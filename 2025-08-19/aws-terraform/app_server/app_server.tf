resource "aws_instance" "app_server" {
  ami           = "ami-042b4708b1d05f512"
  instance_type = "t3.small"
  vpc_security_group_ids = var.sg_from_module
  subnet_id = var.subnet_from_module
  tags = {
    Name = "ExampleAppServerInstance"
  }
}