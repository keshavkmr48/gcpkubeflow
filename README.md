# gcpkubeflow
Kubeflow and Kubeflow pipelines for End2End ML Projects on GCP

### Services Used 
1. Docker
2. Google Cloud Composer / Airflow
3. Google Cloud Build
4. Google Container Registry / Artifact Registry
5. gcloud cli
6. GCS Bucket & Cloud Logging/ Alerting
7. Google Cloud Run & Functions
8. Vertex AI
    - Model Training Service
    - Model Registry
    - Vertex AI endpoints
    - Experiments
    - Explainability
    - Hyperparameter Jobs
    - Feature Store
    - Kubeflow (Pipelines)

### Continuous Integration
    -  Source Code versioning Repository
    - Automated Build
    - Automated Testing

### Continuous Delivery/Deployment
    - Continuous Deployments to Production Environments
    - Monitoring and Alerting

### Google Container and Artifact Registry
    - Artifact Registry for software packages and docker both.
    - Container Registry for docker images only

    Necessary APIs
        - Container and Artifact Registry APIs
        - Cloud Build API

### Google Cloud Run
    - Serverless. Infrastructure provisioning, maintenance , scaling and logging are all automated.
    - Containerized application to facilitate consistency across environments and auto scaling. 
    - Integration with Google Cloud Build helps in seamless CI/CD operations.

    Applications
        - As it is http based, popular for web applications
        - Internal micro services or external facing APIs.
        - Data Processing and ETL : executes ETL jobs on event. 
        - ML model serving. Achieve low latency predictions using auto-scaling based on incoming volume requests.

