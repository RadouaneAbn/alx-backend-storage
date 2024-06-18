#!/usr/bin/env python3
""" 8-all.py """


def list_all(mongo_collection):
    """ This script list all documents in a collection """
    return mongo_collection.find()
