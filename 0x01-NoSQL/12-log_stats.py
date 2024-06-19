#!/usr/bin/env python3
""" 12-log_stats.py """

from pymongo import MongoClient


def get_nginx_stats():
    """ This script provides some stats about nginx logs. """
    client = MongoClient("mongodb://127.0.0.1:27017")
    logs = client.logs.nginx
    print("{} logs".format(logs.count_documents({})))
    print("Methods:")
    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        print("\tmethod {}: {}".format(method, logs.count_documents(
            {"method": method})))
    print("{} status check".format(logs.count_documents(
        {"method": "GET", "path": "/status"})))


if __name__ == "__main__":
    get_nginx_stats()
