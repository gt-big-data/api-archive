from pymongo import MongoClient
from os import environ

USER = environ['MONGODB_USER']
PASS = environ['MONGODB_PASS']
URI = environ['MONGODB_URI']


client = MongoClient("mongodb+srv://{0}:{1}@{2}".format(USER, PASS, URI))
counties_db = client['counties']

if __name__ == '__main__':
    print(client.test)
