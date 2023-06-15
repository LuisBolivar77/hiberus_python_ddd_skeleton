from pymongo import MongoClient
import os


class MongoDBClient:

    @staticmethod
    def db_client():
        mongo_pwd = os.environ.get('MONGODB_PWD')
        mongo_string = os.environ.get('MONGODB_STRING')
        mongo_string = mongo_string.replace('<password>', mongo_pwd)
        mongo_db = os.environ.get('MONGODB_DB')
        client = MongoClient(mongo_string)
        return client[mongo_db]
