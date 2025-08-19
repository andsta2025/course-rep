resource "aws_db_instance" "database1" {
  allocated_storage    = 5
  engine               = "mysql"
  instance_class       = "db.t3.micro"
  engine_version       = "8.0.42"
  username             = "admin"
  password             = "notasecurepassword"
  parameter_group_name = "default.mysql8.0"
  skip_final_snapshot  = true
} 