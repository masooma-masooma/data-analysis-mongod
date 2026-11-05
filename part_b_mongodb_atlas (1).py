import os

import pandas as pd
from pymongo import MongoClient
from urllib.parse import quote_plus

# Credentials are read from environment variables, never written in the code.
# Set them before running, for example in a Windows command prompt:
#   set MONGO_USER=your_username
#   set MONGO_PASSWORD=your_password
#   set MONGO_CLUSTER=your-cluster.xxxxx.mongodb.net
username = quote_plus(os.environ["MONGO_USER"])
pwd = quote_plus(os.environ["MONGO_PASSWORD"])
cluster = os.environ["MONGO_CLUSTER"]

uri = f"mongodb+srv://{username}:{pwd}@{cluster}/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("You are successfully connected to MongoDB!")
except Exception as e:
    print(e)


# load the file using pandas
happiness_df = pd.read_csv('World_Happiness_2019.csv')
covid_df = pd.read_csv('WHO COVID-19 data.csv')
