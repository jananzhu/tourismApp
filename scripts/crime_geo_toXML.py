#!/usr/bin/env python

import sys, os
from elementtree.SimpleXMLWriter import XMLWriter

par_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_dir = os.path.join(par_dir, "derived_data")

def main():
    fout_name = os.path.join(data_dir, "geo_coordinates.xml")
    fout = open(fout_name, "w")
    w = XMLWriter(fout)

    w.start("root")
    f_name = os.path.join(data_dir, "crime_geo_coordinates.txt")
    with open(f_name) as f:
        for line in f:
            lat = str(line.split(",")[0])
            lng = str(line.split(",")[1])

            w.start('dataelement')
            w.element('text', "")
            w.start("geodata")
            w.element("latitude", lat)
            w.element("longitude", lng)
            w.end("geodata")
            w.end("dataelement")
            
    w.end("root")





if __name__ == "__main__":
    main()
