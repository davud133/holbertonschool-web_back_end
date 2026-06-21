#!/usr/bin/env python3
"""Module that contains the function schools_by_topic"""
from pymongo import MongoClient


def schools_by_topic(mongo_collection, topic):
    """Returns the list of schools by topic"""
    return list(mongo_collection.find({ "topics": topic }))
