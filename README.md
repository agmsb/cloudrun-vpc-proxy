# Cloud Run as a VPC Proxy

No more creating a VM and futzing around with SSH to get a client :)

## Build with Buildpacks and Cloud build

```
gcloud alpha builds submit --pack image=gcr.io/$PROJECT_ID/cloudrun
-vpc-proxy
```

## TODO

- Gcloud commands for subnet creation & enabling VPC Serverless Access
- Handle more complex paths
- Pretty print response
