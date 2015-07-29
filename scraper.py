import pandas as pd

import urllib
import urllib.request
import zipfile

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
    df = pd.read_csv(filepath, header=0)
    print(df.to_json())

# Given the year and month, returns a string representation of the custom filepath
def filepath(year, month):
    if month < 10:
        return "csv/%d-0%d-Citi_Bike_trip_data.csv" % (year, month)
    else:
        return "csv/%d-%d-Citi_Bike_trip_data.csv" % (year, month)

if __name__ == "__main__":
    year, month = 2013, 7
    retrieve(year, month)
    stop = [2015, 7]
    while [year, month] != stop:
        print(month, year)
        retrieve(year, month)
        month += 1
        if month == 13:
            month = 1
            year += 1
