# A class to handle the mongodb database
from pymongo import MongoClient
import pandas as pd

class Database:
    def __init__(self, host, port, username, password, database, collection=None):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.database = database
        if collection:
            self.collection = collection

        self.client = MongoClient(self.host, self.port, username=self.username, password=self.password)
        self.db = self.client[self.database]


    # def connect(self):
    #     self.client = MongoClient(self.host, self.port, username=self.username, password=self.password)
    #     self.db = self.client[self.database]

    def disconnect(self):
        self.client.close()

    def test_connection(self):
        try:
            self.client.server_info()
            return True
        except:
            return False
        
    # Insert a dataframe into the database
    def insert(self, stock_name: str, data: pd.DataFrame):
        self.db[stock_name].insert_many(data.to_dict('records'))

    # get the whole collection
    def get_collection(self, stock_name: str):
        return self.db[stock_name].find()