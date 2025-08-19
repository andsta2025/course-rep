resource "aws_db_instance" "database" {
  allocated_storage = 5
  engine            = "mysql"
  instance_class    = "db.t3.micro"
  engine_version    = "8.0.42"
username            = var.db_username
password            = var.db_password
  skip_final_snapshot  = true
}