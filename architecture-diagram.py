from diagrams import Cluster, Diagram, Edge
from diagrams.aws.compute import ECS, ECR, Fargate
from diagrams.aws.network import InternetGateway, ALB, CloudFrontStreamingDistribution
from diagrams.aws.security import IAM, IAMRole
from diagrams.k8s.rbac import User
from diagrams.aws.general import User


with Diagram("AWS ECS architecture diagram", outformat="png", direction="TB"):
  ecr = ECR("Public Container Registry")
  url = User("End User")
  with Cluster("AWS Cloud"):
    with Cluster("VPC Amazon ECS"):
       ecscp = ECS("ECS Cluster")
       appservice = Fargate("App Service")
    with Cluster("VPC Cloud environment"):
      with Cluster("Availability Zone 1"):
        with Cluster("Private Subnet"):
           docker1 = Fargate("Docker container")
      with Cluster("Availability Zone 2"):
           with Cluster("Private Subnet"):
            docker2 = Fargate("Docker container")
    InternetGateway("Internet Gateway")
 
    

    iamserv = IAM("Identity Management")
    additroles = [IAMRole("Role for ECS Cluster"), IAMRole("Role for ECS Task Execution")]
    iamserv >> additroles

    alb_group = CloudFrontStreamingDistribution("LB Group")
    alb = ALB("ALB")

    pubngsg = docker1 - Edge(color="orange", style="dashed") - docker2
    appservice - Edge(color="firebrick", style="dashed") - docker1
    appservice - Edge(color="firebrick", style="dashed") - docker2
    alb - alb_group
    docker1 << alb_group >> docker2
    alb_group << url