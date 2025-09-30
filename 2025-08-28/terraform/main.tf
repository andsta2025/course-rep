# --- Networking ---
from_port = 22
to_port = 22
protocol = "tcp"
cidr_blocks = [var.allowed_ssh_cidr]
}


ingress {
description = "HTTP"
from_port = 80
to_port = 80
protocol = "tcp"
cidr_blocks = ["0.0.0.0/0"]
}


ingress {
description = "HTTPS"
from_port = 443
to_port = 443
protocol = "tcp"
cidr_blocks = ["0.0.0.0/0"]
}


ingress {
description = "Gatus"
from_port = 8080
to_port = 8080
protocol = "tcp"
cidr_blocks = ["0.0.0.0/0"]
}


egress {
from_port = 0
to_port = 0
protocol = "-1"
cidr_blocks = ["0.0.0.0/0"]
}


tags = merge(var.tags, { Name = "${var.project}-sg" })
}


# --- Compute ---
# Ubuntu 24.04 LTS AMI (filter by name; region-specific)
data "aws_ami" "ubuntu" {
most_recent = true
owners = ["099720109477"] # Canonical
filter {
name = "name"
values = ["ubuntu/images/hvm-ssd/ubuntu-noble-24.04-amd64-server-*"]
}
}


resource "aws_instance" "vm" {
ami = data.aws_ami.ubuntu.id
instance_type = var.instance_type
subnet_id = aws_subnet.public.id
vpc_security_group_ids = [aws_security_group.vm.id]
key_name = var.ssh_key_name
associate_public_ip_address = true


tags = merge(var.tags, { Name = "${var.project}-vm" })
}