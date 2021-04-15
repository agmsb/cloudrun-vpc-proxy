# Cloud Run as a VPC Proxy

No more creating a VM and futzing around with SSH to get a client :)

## Create a subnet for VPC Serverless Access

```
gcloud compute networks subnets create cloudrun-vpc-proxy \
--network=default \
--range=172.16.0.0/28 \
--region=$REGION
```

## Enable VPC Serverless Access

```
gcloud services enable vpcaccess.googleapis.com
```
```
gcloud beta compute networks vpc-access connectors create cloudrun-vpc-proxy-connector \
--region=$REGION \
--subnet=$SUBNET
```
## Build with Buildpacks and Cloud Build

No Dockerfile needed!

```
$ gcloud alpha builds submit --pack image=gcr.io/$PROJECT_ID/cloudrun
-vpc-proxy
```

## Deploy to Cloud Run
```
gcloud run deploy cloudrun-vpc-proxy \
--image gcr.io/$PROJECT_ID/cloudrun-vpc-proxy \
--vpc-connector=cloudrun-vpc-proxy-connector \
--vpc-egress=private-ranges-only
```

## Issue request to Cloud Run

You probably want to make sure this is only available to authenticated users in Cloud Run.

```
$ curl -H "Authorization: Bearer $(gcloud auth print-identity-token)" $CLOUD_RUN_ENDPOINT/ip_addr/$PRIVATE_IP
```

## TODO

- handle more complex paths
- pretty print response