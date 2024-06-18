#!/usr/bin/env python3
""" 10-update_topics.py """


def update_topics(mongo_collection, name, topics):
    """ This script updates a document """
    mongo_collection.update_one({"name": name}, {"$set": {"topics": topics}})
