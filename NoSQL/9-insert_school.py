#!/usr/bin/env python3
"""Module that contains the function insert_school"""
from pymongo import MongoClient


def insert_school(mongo_collection, **kwargs):
    """Inserts a new document into a collection based on kwargs"""
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
