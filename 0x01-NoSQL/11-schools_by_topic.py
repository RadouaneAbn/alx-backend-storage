#!/usr/bin/env python3
""" 11-schools_by_topic.py """


def schools_by_topic(mongo_collection, topic):
    """ This script return the list of schools having a specific topic """
    return mongo_collection.find({"topics": {"$in": [topic]}})
