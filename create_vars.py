#!/usr/bin/env python3

from email.policy import default
import sys
import os
import csv
import json

def main():

    devices = []
    with open(os.path.join(sys.path[0],'address.csv'), 'r') as vars_:
        for line in csv.DictReader(vars_):
            devices.append(line)
    data = devices

    with (open("vars.tf", "w")) as f:
        f.write("variable \"test\" { \n  default = {")

    with open('vars.tf', 'a') as f:
        for i in data:
            f.write('\n    {} = '.format(i['name']))
            json.dump(i, f, indent=6, separators=[",", " = "])
        f.write('\n}\n}')

if __name__ == '__main__':
   main()