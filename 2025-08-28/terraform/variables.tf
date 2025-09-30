variable "project" { type = string }
variable "aws_region" { type = string default = "eu-central-1" }
variable "vpc_cidr" { type = string default = "10.42.0.0/16" }
variable "public_subnet_cidr" { type = string default = "10.42.1.0/24" }
variable "instance_type" { type = string default = "t3.micro" }
variable "ssh_key_name" { type = string description = "Existing AWS key pair name" }
variable "allowed_ssh_cidr" { type = string default = "0.0.0.0/0" }
variable "tags" {
type = map(string)
default = {}
}