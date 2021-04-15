# Cloud Run as a VPC Proxy

No more creating a VM and futzing around with SSH to get a client :)

## Build with Buildpacks and Cloud Build

No Dockerfile needed!

```
$ gcloud alpha builds submit --pack image=gcr.io/$PROJECT_ID/cloudrun
-vpc-proxy
```
## Issue request to Cloud Run

You probably want to make sure this is only available to authenticated users in Cloud Run.

```
$ curl -H "Authorization: Bearer $(gcloud auth print-identity-token)" $CLOUD_RUN_ENDPOINT/ip_addr/$PRIVATE_IP
```

## TODO

- gcloud for cloud run deploy
- gcloud for subnet creation
- gcloud for enabling VPC Serverless Access
- handle more complex paths
- pretty print response