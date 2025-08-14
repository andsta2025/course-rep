terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.38"
    }
  }
  required_version = ">= 1.2.0"
}

provider "aws" {
  region = "eu-north-1"
}

resource "aws_instance" "app_server" {
  ami           = "ami-042b4708b1d05f512"
  instance_type = "t3.small"
  tags = {
    Name = "ExampleAppServerInstance"
  }
}