#!/usr/bin/env python3
""" 101-students.py """


def top_students(mongo_collection):
    """ This script returns all students sorted by average score """
    students = mongo_collection.aggregate([
        {"$unwind": "$topics"},
        {"$group": {
            "_id": {
                "_id": "$_id",
                "name": "$name"
            },
            "averageScore": {"$avg": "$topics.score"}
        }},
        {"$sort": {"averageScore": -1}},
        {"$project": {
            "_id": "$_id._id",
            "name": "$_id.name",
            "averageScore": "$averageScore"
        }}
    ])
    return students
