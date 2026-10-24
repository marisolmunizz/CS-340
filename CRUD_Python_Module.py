from pymongo import MongoClient
from bson.objectid import ObjectId


class AnimalShelter(object):
    """CRUD operations for Animal collection in MongoDB."""

    def __init__(self, username, password):
        HOST = 'localhost'
        PORT = 27017
        DB = 'aac'
        COL = 'animals'

        self.client = MongoClient(
            'mongodb://%s:%s@%s:%d/?authSource=admin'
            % (username, password, HOST, PORT)
        )
        self.database = self.client[DB]
        self.collection = self.database[COL]

    # Create method to implement the C in CRUD.
    def create(self, data):
        if not isinstance(data, dict) or not data:
            return False

        try:
            result = self.collection.insert_one(data)
            return result.acknowledged
        except Exception as error:
            print("Create failed:", error)
            return False

    # Read method to implement the R in CRUD.
    def read(self, query):
        if not isinstance(query, dict):
            return []

        try:
            return list(self.collection.find(query))
        except Exception as error:
            print("Read failed:", error)
            return []

    # Update method to implement the U in CRUD.
    def update(self, query, new_values):
        if not isinstance(query, dict) or not isinstance(new_values, dict):
            return 0

        try:
            result = self.collection.update_many(
                query,
                {"$set": new_values}
            )
            return result.modified_count
        except Exception as error:
            print("Update failed:", error)
            return 0

    # Delete method to implement the D in CRUD.
    def delete(self, query):
        if not isinstance(query, dict):
            return 0

        try:
            result = self.collection.delete_many(query)
            return result.deleted_count
        except Exception as error:
            print("Delete failed:", error)
            return 0