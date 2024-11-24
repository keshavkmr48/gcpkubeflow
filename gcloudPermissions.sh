# assign service account user role to the service account
gcloud projects add-iam-policy-binding clv-03091991-vertexai --member=serviceAccount:991170270785@cloudbuild.gserviceaccount.com --role=roles/iam.serviceAccountUser

# assign cloud run role to the service account
gcloud projects add-iam-policy-binding clv-03091991-vertexai --member=serviceAccount:991170270785@cloudbuild.gserviceaccount.com --role=roles/run.admin