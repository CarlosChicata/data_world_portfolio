terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "4.30.0"
    }
  }
}

provider "google" {
  credentials = file("data-world-portfolio-gsaccount.json")

  project     = var.project
  region      = var.region
}


# Compress source code, NOTE: separate env in separated folder in project
data "archive_file" "code_function" {
  type        = "zip"
  source_dir  = "../src"
  output_path = "./compress_code.zip"
}

# Create bucket that will host the source code
resource "google_storage_bucket" "bucket" {
  name 		= "${var.project}-compressed-code-functions"
  location	= var.region
}

# Add source code zip to bucket
resource "google_storage_bucket_object" "zip" {
  # Append file MD5 to force bucket to be recreated
  name   = "source.zip#${data.archive_file.code_function.output_md5}"
  bucket = google_storage_bucket.bucket.name
  source = data.archive_file.code_function.output_path
}

# Create Cloud Function
resource "google_cloudfunctions_function" "function" {
  name                  = var.name
  runtime               = "python39"
  description           = "cloud function created by terraform"

  available_memory_mb   = 256
  source_archive_bucket = google_storage_bucket.bucket.name
  source_archive_object = google_storage_bucket_object.zip.name
  trigger_http          = true
  entry_point           = var.entry_point
  timeout               = 120
}

# create service account to authenticate to use in function
resource "google_service_account" "invoker_job" {
  account_id	= "function-invoker-in-scheduler"
  display_name	= "Cloud Function Tutorial Invoker Service Account"
  project	= var.project
}

# binding function with service account
resource "google_cloudfunctions_function_iam_member" "invoker" {
  project        = google_cloudfunctions_function.function.project
  region         = google_cloudfunctions_function.function.region
  cloud_function = google_cloudfunctions_function.function.name

  role   = "roles/cloudfunctions.invoker"
  member = "allUsers"
}

resource "google_cloud_scheduler_job" "job" {
  name             = "cloud-function-tutorial-scheduler"
  description      = "Trigger the ${google_cloudfunctions_function.function.name} Cloud Function every 10 mins."
  schedule         = "0 * * * *" # Every 10 mins
  time_zone        = "America/Lima"
  attempt_deadline = "320s"

  http_target {
    http_method = "POST"
    uri         = google_cloudfunctions_function.function.https_trigger_url

    oidc_token {
      service_account_email = google_service_account.invoker_job.email
    }
  }
}
