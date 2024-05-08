#!/usr/bin/env python3
"""Update a document in Python"""


def update_topics(mongo_collection, name, topics):
    """Update a document in Python"""
    mongo_collection.update({"name": name}, {"$set": {"topics": topics}},{multi: true})
    return mongo_collection
