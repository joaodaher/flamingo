![Build Status](https://github.com/flamingo-run/flamingo/workflows/Github%20CI/badge.svg)
[![Maintainability](https://api.codeclimate.com/v1/badges/50d9f44092cbc7ee4308/maintainability)](https://codeclimate.com/github/flamingo-run/flamingo/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/50d9f44092cbc7ee4308/test_coverage)](https://codeclimate.com/github/flamingo-run/flamingo/test_coverage)
[![python](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/)

# Flamingo


## Deployment

It's recommended to use Google Cloud Build to deploy the Flamingo Server application to Cloud Run

For this, you'll need to add 2 Variables to the build configuration: `_GIT_ACCESS_TOKEN` and `URL` (see **Environment Variables** section for more info)

### Option A: Use Run on Google Cloud button
[![Run on Google Cloud](https://deploy.cloud.run/button.svg)](https://deploy.cloud.run)

### Option B: Create your own deployment

Create a new Cloud Build trigger selecting the option ``Cloud Build configuration file (yaml or json)``


# Setup

- Create a service account for Flamingo: he's your new DevOps.
- Add this account email to all the projects you want Flamingo to manage:
   - `Cloud Build Editor`
   - `Cloud SQL Admin`
   - `Container Registry Service Agent`
   - `Service Account Admin`
   - `Service Account User`
   - `Project IAM Admin`
   - `Cloud Run Admin`
   - `Secret Manager Admin`
   - `Source Repository Administrator`
   - `Storage Admin`
   - `Cloud Datastore Admin`
   - `Pub/Sub Admin`
- [Enable Firestore](https://console.cloud.google.com/firestore/data) using Datastore mode: needed to store Flamingo's data
- [Enable Resource Manager](https://console.developers.google.com/apis/library/cloudresourcemanager.googleapis.com): needed to manage app's permissions
- [Enable IAM](https://console.developers.google.com/apis/api/iam.googleapis.com/overview): needed to manage app's service account
- [Enable Cloud SQL](https://console.developers.google.com/apis/api/sqladmin.googleapis.com/overview): needed to manage app's SQL database
- [Enable App Engine Admin](https://console.developers.google.com/apis/api/appengine.googleapis.com/overview): needed to fetch project's default location
- Deploy Flamingo as the service account create previously


# Environment Variables

- FLAMINGO_URL: the public URL of the service to receive build hooks
- GIT_ACCESS_TOKEN: add the personal access token to allow build notification with code diff
