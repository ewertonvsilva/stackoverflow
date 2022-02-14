> gcloud beta composer environments run $composer \
  --location $location \
  variables set -- \
  project_id $project
  
  > gcloud beta composer environments run $composer \
  --location $location \
  variables set -- \
  gce_zone $gce_zone
  
  > gcloud beta composer environments run $composer \
  --location $location \
  variables set -- \
  bucket_path $bucket_path
