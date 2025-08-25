terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 6.0"
    }
  }
  required_version = ">= 1.6.0"
}

provider "aws" {
  region = "eu-north-1"
}

resource "aws_s3_bucket" "example" {}

resource "aws_instance" "app_server" {
  ami           = "ami-042b4708b1d05f512"
  instance_type = "t3.small"
  tags = {
    Name = "app-server"
  }
  depends_on = [aws_s3_bucket.example]
}




