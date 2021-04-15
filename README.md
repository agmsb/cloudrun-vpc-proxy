# Cloud Run as a VPC Proxy

No more creating a VM and futzing around with SSH to get a client :)

## Build with Buildpacks and Cloud build

```
 gcloud alpha builds submit --pack image=gcr.io/agmsb-k8s/cloudrun
-vpc-proxy```