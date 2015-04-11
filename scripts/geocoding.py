#!/usr/bin/env python

import os
import requests

# Get API Key from separate file
API_KEY = ""

with open("apikey.text") as f:
    for line in f:
        if line.startswith("google"):
            API_KEY = line.split("=")[1].strip()

API_ADDRESS = "https://maps.googleapis.com/maps/api/geocode/json?"

def main():
    # Path to datafiles
    par_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_dir = os.path.join(par_dir, "derived_data")

    # Addresses saved to list
    addresses = []
    with open("../derived_data/crime_addresses_dc_short.txt") as f:
        for line in f:
            addresses.append(line)

    # Write geo coordinates to file
    fout = open(data_dir + os.path.sep + "crime_geo_coordinates.txt", "w")

    # Dictionary to hold query parameters
    parameters = {"address": None, "key": API_KEY}

    for address in addresses:
        parameters["address"] = address
        r = requests.get(API_ADDRESS, params=parameters)

        # Convert to json from request
        j = r.json()

        geometry = j["results"][0]["geometry"]["location"]
        lat = j["results"][0]["geometry"]["location"]["lat"]
        lng = j["results"][0]["geometry"]["location"]["lng"]
        str_to_write = str(lat) + "," + str(lng) + "\n"
        fout.write(str_to_write)
    
if __name__ == "__main__":
    main()
