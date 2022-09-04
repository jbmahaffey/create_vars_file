variable "test_ip" { 
  default = {
    test1 = {
      "name" = "test1",
      "type" = "ipmask",
      "subnet" = "1.1.1.0",
      "mask" = "255.255.255.0",
      "allow_routing" = "false"
}
    test2 = {
      "name" = "test2",
      "type" = "ipmask",
      "subnet" = "2.2.2.0",
      "mask" = "255.255.255.0",
      "allow_routing" = "false"
}
    test3 = {
      "name" = "test3",
      "type" = "ipmask",
      "subnet" = "3.3.3.3",
      "mask" = "255.255.255.255",
      "allow_routing" = "false"
}
}
}


variable "test_fqdn" { 
  default = {
    msn = {
      "name" = "msn",
      "type" = "fqdn",
      "fqdn" = "msn.com",
      "allow_routing" = "false"
}
    hbo = {
      "name" = "hbo",
      "type" = "fqdn",
      "fqdn" = "hbo.com",
      "allow_routing" = "false"
}
}
}