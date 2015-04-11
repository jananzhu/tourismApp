#!/usr/bin/env python

import os
import requests

with open("apikey.txt") as f:
    for line in f:
        if line.startswith("google"):
            API_KEY = line.split("=")[1].strip()

API_ADDRESS = "https://maps.googleapis.com/maps/api/geocode/json?"

def main():

    parameters = {"address": "1500 - 1599 BLOCK OF 1ST STREET SW, Washington DC","key":API_KEY} 
    r = requests.get(API_ADDRESS, params=parameters)
    j = r.json()
    geometry = j["results"][0]["geometry"]["location"]
    lat = j["results"][0]["geometry"]["location"]["lat"]
    lng = j["results"][0]["geometry"]["location"]["lng"]
    print lat, lng


if __name__ == "__main__":
    main()
