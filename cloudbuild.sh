# build docker image 
docker build -t gcpmlops-app .

# push docker image to gcr artifact repository

docker tag gcpmlops-app us-docker.pkg.dev/clv-03091991-vertexai/gcpllmops/gcpmlops-app
docker push us-docker.pkg.dev/clv-03091991-vertexai/gcpllmops/gcpmlops-app




# deploy app after pulling image from artifact registry to cloud run
gcloud run deploy gcpmlops-app-deployment \
    --image us-docker.pkg.dev/clv-03091991-vertexai/gcpllmops/gcpmlops-app \
    --region us-east1 \
    --timeout 300