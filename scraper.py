import pandas as pd

import csv
import json
import urllib
import urllib.request
import zipfile

# Given the year and month, returns a string representation of the custom filepath
def filepath(year, month):
    if month < 10:
        return "csv/%d-0%d - Citi Bike trip data.csv" % (year, month)
    else:
        return "csv/%d-%d - Citi Bike trip data.csv" % (year, month)

# Will retrieve the specified dataset from the Citi Bike System Data website
def retrieve(year, month):
    url = "https://s3.amazonaws.com/tripdata/"
    if month < 10:
        url += "%d0%d-citibike-tripdata.zip" % (year, month)
    else:
        url += "%d%d-citibike-tripdata.zip" % (year, month)
    print(url)
    local_file, headers = urllib.request.urlretrieve(url)
    with zipfile.ZipFile(local_file) as zf:
        zf.extractall('csv/')

def scrape(filepath):
    print("Scraping data from %s..." % (filepath))
    header = ["tripduration", "starttime", "stoptime",
              "start station id", "start station name", "start station latitude", "start station longitude",
              "end station id", "end station name", "end station latitude", "end station longitude",
              "bikeid", "usertype", "birth year", "gender"]

    csvfile = open(filepath, 'r')
    reader = csv.DictReader(csvfile)
    data = []
    for each in reader:
        row = {}
        for field in header:
            row[field] = each[field]
        data.append(row)#df = pd.read_csv(filepath, header=0)
    print("...done")
    return data

if __name__ == "__main__":
    scrape(filepath(2014, 7))
    '''year, month = 2013, 7
    retrieve(year, month)
    stop = [2015, 7]
    while [year, month] != stop:
        print(month, year)
        retrieve(year, month)
        month += 1
        if month == 13:
            month = 1
            year += 1
    '''
