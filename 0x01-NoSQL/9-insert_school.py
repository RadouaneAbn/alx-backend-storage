#!/usr/bin/env python3
""" 9-insert_school.py """


def insert_school(mongo_collection, **kwargs):
    """ This script inserts a document """
    return mongo_collection.insert_one(kwargs)
