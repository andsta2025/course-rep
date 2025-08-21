variable "project" {
  description = "Map of project names to configuration."
  type        = map(any)
  default = {
    client-webapp = {
      instance_type = "t3.small",
      environment   = "dev"
    },
    internal-webapp = {
      instance_type = "t3.micro",
      environment   = "test"
    }
  }
}
variable "create" {
  description = "True if we want to create it"
  type        = string
  default     = false
}