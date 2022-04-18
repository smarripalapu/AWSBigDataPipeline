# AWSBigDataPipeline

Create big data processing pipeline. Explore use of tools such as Kafka or AWS Kinesis and AWS DynamoDB or EMR to accepts and process data in real-time or “simulated” real time.

## Docker image build steps for mac m1:
ECR (Elastic Container Registry) REPOSITORY: s3dynamo \n
Open the repository to view push commands as below. \n 

1) docker build -t s3dynamo . --platform=linux/amd64 \n
2) docker tag s3dynamo:latest 333930370422.dkr.ecr.us-east-1.amazonaws.com/s3dynamo:v1
3) docker push 333930370422.dkr.ecr.us-east-1.amazonaws.com/s3dynamo:v1
