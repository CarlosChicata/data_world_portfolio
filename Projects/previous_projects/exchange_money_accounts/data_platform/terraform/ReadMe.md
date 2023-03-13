# Infrastructure-as-code in Data platform
This folder explain how implement "Data platform". I use terraform to implement all resource in my GCP account.

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

