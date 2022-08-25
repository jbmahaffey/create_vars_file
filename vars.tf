variable "test" { 
default = {
 test1 = {
    "name" = "test1",
    "type" = "ipmask",
    "subnet" = "1.1.1.0",
    "mask" = "255.255.255.0",
    "fqdn" = "",
    "allow-routing" = "false"
}
 test2 = {
    "name" = "test2",
    "type" = "ipmask",
    "subnet" = "2.2.2.0",
    "mask" = "255.255.255.0",
    "fqdn" = "",
    "allow-routing" = "false"
}
 test3 = {
    "name" = "test3",
    "type" = "ipmask",
    "subnet" = "3.3.3.3",
    "mask" = "255.255.255.255",
    "fqdn" = "false",
    "allow-routing" = null
}
 msn = {
    "name" = "msn",
    "type" = "fqdn",
    "subnet" = "",
    "mask" = "msn.com",
    "fqdn" = "false",
    "allow-routing" = null
}
}
}