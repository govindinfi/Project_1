# AWS ECS Cluster Deployment with Terraform
This repository demonstrates how to deploy an AWS ECS cluster using Terraform, utilizing the public Docker NGINX image for container deployment.

## Steps

Clone the main project repository.

Create an AWS access key and secret key, then store them in the main.tf. You can utilize the AWS CLI for this process.

Run the command `terraform init` to install the required providers.

Run the command `terraform plan` to assess the status of the defined resources provisioning.

Run the command `terraform apply` to provision the defined resources.

## Architecture Diagram

For a visual representation of the deployment architecture, refer to the following diagram created using diagrams:

(https://github.com/mingrammer/diagrams)

<img src="https://github.com/govindinfi/Project_1/blob/main/aws_ecs_architecture_diagram.png" width="900" />

Thank you!
