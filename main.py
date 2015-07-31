import MongoWrapper
import scraper

MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017
DB_NAME = 'CitiBike'
COLLECTION_NAME = 'historical'

wrapper = MongoWrapper.MongoWrapper(MONGODB_HOST, MONGODB_PORT, DB_NAME)
year, month = 2014, 9
#wrapper.clear(COLLECTION_NAME)

# Loop through csv's and insert all into MongoDB
stop = [2015, 7]
while [year, month] != stop:
    print(month, year)
    wrapper.add(COLLECTION_NAME, scraper.scrape(scraper.filepath(year, month)))
    month += 1
    if month == 13:
        month = 1
        year += 1
    wrapper.test(COLLECTION_NAME)
