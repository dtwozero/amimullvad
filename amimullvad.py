#!/usr/bin/python

import json
import requests
import os
from termcolor import colored

# Define API url:

response = requests.get("https://am.i.mullvad.net/json")
data = response.json()

# Define a bunch of variables because termcolor doesn't work with json objects
try:
    newip = data["ip"]
    country = data["country"]
    city = str(data["city"])
    mullserv = data["mullvad_server_type"]
    latitude = str(data["latitude"])
    longitude = str(data["longitude"])
    mullxip = str(data["mullvad_exit_ip"]) # this is going to be True/False
    mullxhost = data["mullvad_exit_ip_hostname"]
    organization = data["organization"]
except:
    print("nope")

# Print the info we need to the screen

os.system('clear')
try:
    os.system('figlet am.i.mullvad')
except:
    print(colored("You must install figlet from your Linux Distros Repo.", 'red'))

print("Author: " + colored("Twitter: @dTwoZ3r0", 'red'))
print("")
try:
    print("IP: " + colored(newip, 'green'))
    print("Country: " + colored(country, 'green'))
    if city == 'None':
        print("City: " + colored(city, 'red'))
    else:
        print("City: " + colored(city, 'green'))
    print("Latitude: " + colored(latitude, 'yellow'))
    print("Longitude: " + colored(longitude, 'yellow'))
    if mullxip == False:
        print("Mullvad Exit IP: " + colored(mullxip, 'red'))
    else:
        print("Mullvad Exit IP: " + colored(mullxip, 'green'))
    print("Mullvad Exit IP Hostname: " + colored(mullxhost, 'green'))
    print("Organization: " + colored(organization, 'green'))
    print("Mullvad Server Type: " + colored(mullserv, 'green'))
    print("")
    print("To proxy firefox: " + colored("https://mullvad.net/en/servers/#wireguard ", 'green') + "and check Proxy DNS box")
except:
    print(colored("You ARE NOT connected to mullvad!!", 'red'))
