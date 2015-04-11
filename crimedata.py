#!/usr/bin/python

import os, sys
import xml.etree.ElementTree as etree



def main():
    obj = etree.parse(raw_data_dir + os.path.sep +"crime_incidents_2013_plain.xml")
    root = obj.getroot()
    f = open(derived_data_dir + os.path.sep + "crime_addresses.txt", 'w')
    for child in root:
        f.write(child[6].text + "\n")
    return




if __name__ == "__main__":
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    raw_data_dir = os.path.join(parent_dir, "raw_data")
    derived_data_dir = os.path.join(parent_dir, "derived_data")
    main()
