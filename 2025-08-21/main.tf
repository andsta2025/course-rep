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
resource "aws_eip" "ip" {
  instance = aws_instance.app_server.id
}
resource "aws_instance" "for_each_example" {
  for_each = var.project
  ami = "ami-042b4708b1d05f512"
  instance_type = each.value.instance_type
  tags = {
    Name = each.value.environment
  }
}
resource "aws_instance" "if_example" {
  count         = var.create == "true" ? 1 : 0
  ami           = "ami-042b4708b1d05f512"
  instance_type = "t3.micro"
  lifecycle {
    prevent_destroy = false
  }
}





