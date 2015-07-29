from pymongo import MongoClient

class MongoWrapper():
    # Upon initialization, MongoWrapper will establish a connection
    # to the specified database. Specific collections will be
    # retrieved on a per-method basis.
    def __init__(self, host, port, database):
        #Pass variables to connect to proper MongoDB database
        self.MONGODB_HOST = host
        self.MONGODB_PORT = port
        self.DB_NAME = database
        self.CONNECTION = MongoClient(self.MONGODB_HOST, self.MONGODB_PORT)

    def test(self, collection_name, fields):
        try:
            collection = self.CONNECTION[self.DB_NAME][collection_name]
            row = collection.find_one(projection=fields)
            print(row)
        except Exception as e:
            print(str(e))

    # variable 'data' must be a list of dictionaries
    def add(self, collection_name, data):
        msg = "Inserting data into %s collection..." % (collection_name)
        print(msg)
        try:
            collection = self.CONNECTION[self.DB_NAME][collection_name]
            collection.insert(data)
            print("...done.")
        except Exception as e:
            print(str(e))

    def clear(self, collection_name):
        try:
            msg = "Dropping collection %s from %s database..." % (collection_name, self.DB_NAME)
            print(msg)
            collection = self.CONNECTION[self.DB_NAME][collection_name]
            collection.drop()
            print("...done")
        except Exception as e:
            print(str(e))

    '''def export_csv():
        print "Exporting to csv..."
        f = open('tweets.csv', 'w', newline = '')
        for tweet in tweets:
            tweet.date = tweet.date.date()
    '''
    #    query = "@Betterment"
    #    scrape(query)
