#!/usr/bin/env python3

import sys
import os
import csv
import json

def main():

# Create IP variables
    devices = []
    with open(os.path.join(sys.path[0],'ip_address.csv'), 'r') as vars_:
        for line in csv.DictReader(vars_):
            devices.append(line)

    with open("vars.tf", "w") as f:
        f.write("variable \"test_ip\" { \n  default = {")

    with open('vars.tf', 'a') as f:
        for i in devices:
            f.write('\n    {} = '.format(i['name']))
            json.dump(i, f, indent=6, separators=[",", " = "])
        f.write('\n}\n}\n\n\n')

# Create fqdn variables
    fqdnlist = []
    with open(os.path.join(sys.path[0],'fqdn_address.csv'), 'r') as vars_:
        for line in csv.DictReader(vars_):
            fqdnlist.append(line)

    with open('vars.tf', 'a') as f:
        f.write("variable \"test_fqdn\" { \n  default = {")

    with open('vars.tf', 'a') as f:
        for i in fqdnlist:
            f.write('\n    {} = '.format(i['name']))
            json.dump(i, f, indent=6, separators=[",", " = "])
        f.write('\n}\n}')

if __name__ == '__main__':
   main()

# May want to add if statement to search dictionary for group name and types and create terraform
# variables based on these groups