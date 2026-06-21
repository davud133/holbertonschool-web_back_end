#!/usr/bin/env python3
"""listing all databases"""


from pymongo import MongoClient


def list_all(mongo_collection):
    """
    Lists all documents in a MongoDB collection.
    """
    if mongo_collection is None:
        return []
    return list(mongo_collection.find())
