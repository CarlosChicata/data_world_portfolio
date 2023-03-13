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

# Create queue to receive events from source systems
resource "google_pubsub_topic" "transaction_queue" {
  name				= "transaction_queue"
  message_retention_duration	= "86600s"
  project			= var.project
}

# create a datalake based in cloud storage
resource "google_storage_bucket" "datalake" {
  name		= var.bucket_name
  location	= var.location
  force_destroy = true
}

# create raw layer for transaction in app of system
resource "google_storage_bucket_object" "raw_layer_transactional" {
  name = "RAW/BANC/ALL/OPE/KAMB/"
  content = "Store data from transactional owned system."
  bucket = "${google_storage_bucket.datalake.name}"
}

# create raw layer for exchange data from external source system
resource "google_storage_bucket_object" "raw_layer_forex_api" {
  name = "RAW/BANC/ALL/FIN/ENTR/EXCHANGE/FOREX/API/"
  content = "Store data from external API system about exchange."
  bucket = "${google_storage_bucket.datalake.name}"
}

