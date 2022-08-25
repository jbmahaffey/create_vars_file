#!/usr/bin/env python3

from email.policy import default
import sys
import os
import requests
import argparse
import yaml
import csv
import ssl
import logging
import json
ssl._create_default_https_context = ssl._create_unverified_context
requests.packages.urllib3.disable_warnings() 

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--fortigate', default='172.17.101.57', help='Firewall IP Address')
    parser.add_argument('--token', default='', help='API Token')
    parser.add_argument('--logging', default='', help='Logging levels info, error, or debug')
    parser.add_argument('--devlist', default='address.csv', help='YAML/CSV file with list of approved devices.')
    args = parser.parse_args()

    # Only enable logging when necessary
    if args.logging != '':
        logginglevel = args.logging
        formattedlevel = logginglevel.upper()

        # Open logfile
        logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s',filename='address.log', level=formattedlevel, datefmt='%Y-%m-%d %H:%M:%S')
    else:
        ()
    
    # Open variable file either csv or yaml
    filetype = args.devlist.split('.')
    
    if filetype[1] == 'yml':
        # Open YAML variable file
        with open(os.path.join(sys.path[0],args.devlist), 'r') as vars_:
            data = yaml.safe_load(vars_)
    
    elif filetype[1] == 'csv':
        devices = []
        with open(os.path.join(sys.path[0],args.devlist), 'r') as vars_:
            for line in csv.DictReader(vars_):
                devices.append(line)
        data = devices


    with (open("vars.tf", "w")) as f:
        f.write("variable \"test\" { \ndefault = {\n")

    with open('vars.tf', 'a') as f:
        for i in data:
            f.write('\n {} = '.format(i['name']))
            json.dump(data[0], f, indent=2, separators=[",", " = "])
        f.write('\n}\n}')

if __name__ == '__main__':
   main()