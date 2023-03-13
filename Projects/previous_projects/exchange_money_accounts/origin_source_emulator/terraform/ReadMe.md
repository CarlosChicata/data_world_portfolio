# Infrastructure-as-code in Origin Source emulator
This file explain how implement "Origin source emulator". I use terraform to implement all resource in my GCP account.

I'll explain:
* Code of terraform to generate resources.
* Common Errors i faced to generate this infrastructure.

If you are new in terraform; this is a great point to start to learn and practice! :smile:

## Explain code of terraform

This section set up my terraform configuration to use GCP and get access my project by service account.
```
terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "4.30.0"
    }
  }
}

provider "google" {
  credentials = file("<file_name.json>")

  project     = var.project
  region      = var.region
}

```


Programmatically enable IAM API in my project.
```
resource "google_project_service" "project" {
  project = var.project
  service = "iam.googleapis.com"

  disable_on_destroy = true
}
```

Generate a zip file contained all files of my code will use by cloud function, then i create a bucket and object based in this zip file.

```
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
```

Generate a cloud function. In this case i used python 3.9

```
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
```

Create a service account to invoke inside of scheduler. i create another service account to invoke my cloud function because by default the Cloud Function can't be invoked by anyone.

```
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
```

Create a scheduler will invoke the cloud function. I used a previous service account to authenticate my calls.

```
resource "google_cloud_scheduler_job" "job" {
  name             = "cloud-function-tutorial-scheduler"
  description      = "Trigger the ${google_cloudfunctions_function.function.name} Cloud Function every 10 mins."
  schedule         = "0 * * * *" # Every 10 mins
  time_zone        = "America/Lima"
  attempt_deadline = "320s"

  http_target {
    http_method = "GET"
    uri         = google_cloudfunctions_function.function.https_trigger_url

    oidc_token {
      service_account_email = google_service_account.invoker_job.email
    }
  }
}
```

## Common errors i faced

### Check your version of provider

I have this error because i was using a old version of google provedor. 

```
Error: Missing required argument
│
│   on main.tf line XX, in resource "google_storage_bucket" "bucket":
│   XX: resource "google_storage_bucket" "bucket" {
│
│ The argument "location" is required, but no definition was found.
```

To solve this project, you need to check the latest version of your proveedor ( or version i will use) and check what fields are required to used in your resources based in documentation.

### Problem in JWT Signature by invalid grant
```
│ Error: Post "https://storage.googleapis.com/storage/v1/b?alt=json&prettyPrint=false&project=data-world-portfolio": oauth2: cannot fetch token: 400 Bad Request
│ Response: {"error":"invalid_grant","error_description":"Invalid JWT Signature."}
│
│   with google_storage_bucket.bucket,
│   on main.tf line XX, in resource "google_storage_bucket" "bucket":
│   XX: resource "google_storage_bucket" "bucket" {
```
This error is based in problem in my key of my service account i used in my terraform configuration. I solved it by i changed my old key with new key of service account.


### IAM is disable 

```
Error: Error creating service account: googleapi: Error 403: Identity and Access Management (IAM) API has not been used in project 40XXXX15XXXX before or it is disabled.
Enable it by visiting https://console.developers.google.com/apis/api/iam.googleapis.com/overview?project=40XXXX15XXXX then retry. 
If you enabled this API recently, wait a few minutes for the action to propagate to our systems and retry., accessNotConfigured
|
|   with google_service_account.service_account,
|   on main.tf line XX, in resource "google_service_account" "service_account":
|   XX: resource "google_service_account" "service_account"
```

This error is generated by your project has disable IAM API. Solution is find IAM API; like below image; and click in "enable" service.

![iam_disable](https://github.com/CarlosChicata/data_world_portfolio/blob/main/Projects/exchange_money_accounts/origin_source_emulator/terraform/IAM_enable_2.png?raw=true)

If you want to automaticated this process; check this [link](https://stackoverflow.com/questions/63358802/how-to-enable-identity-and-access-management-iam-api-programmatically-for-a-go)

### Other errors
You can check this [link](https://github.com/terraform-google-modules/terraform-google-project-factory/blob/master/docs/TROUBLESHOOTING.md) to find other errors that i don't see.

