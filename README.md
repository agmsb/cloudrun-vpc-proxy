# Cloud Run VPC Proxy

Cloud Run as a VPC Proxy is a project to make GCP demos that require connecting to private IPs slightly easier. 

*Lol, please don't use for any other purpose other than demos.*

Cloud Run VPC Proxy will use Serverless VPC Access to ensure that a Cloud Run instance running a Flask app can access private endpoints in your Google VPC.

Cloud Run VPC Proxy works by issuing a request with the Private IP baked into a subpath at `http://$CLOUD_RUN_ENDPOINT/ip_addr/$PRIVATE_IP`. This will issue a request from the Flask app to that private IP and return the response provided from your private app. 

It also by default requires authenticated users, so you will need to pass in a token from an authenticated and authorized IAM user in your GCP project when generating your request.


No more creating a VM and futzing around with SSH to get a client in your VPC network. :)


## Create a subnet for VPC Serverless Access

```
$ gcloud compute networks subnets create cloudrun-vpc-proxy \
--network=default \
--range=172.16.0.0/28 \
--region=$REGION
```

## Enable VPC Serverless Access

```
$ gcloud services enable vpcaccess.googleapis.com
```
```
$ gcloud beta compute networks vpc-access connectors create cloudrun-vpc-proxy-connector \
--region=$REGION \
--subnet=$SUBNET
```
## Build with Buildpacks and Cloud Build

No Dockerfile needed! Buildpacks are magic.

```
$ gcloud alpha builds submit --pack image=gcr.io/$PROJECT_ID/cloudrun
-vpc-proxy
```

## Deploy to Cloud Run

Note that we're passing in the Serverless VPC Connector previously created, and ensuring that we're only going through the connector for requests to private ranges.

```
$ gcloud run deploy cloudrun-vpc-proxy \
--image gcr.io/$PROJECT_ID/cloudrun-vpc-proxy \
--vpc-connector=cloudrun-vpc-proxy-connector \
--vpc-egress=private-ranges-only
```

## Issue request to Cloud Run VPC Proxy

You'll need to make sure that you're authenticated with gcloud to make this request work.

```
$ curl -H "Authorization: Bearer $(gcloud auth print-identity-token)" $CLOUD_RUN_ENDPOINT/ip_addr/$PRIVATE_IP
```

## TODO

- handle more complex paths
- pretty print response