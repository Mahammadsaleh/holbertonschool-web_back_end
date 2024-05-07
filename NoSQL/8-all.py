#!/usr/bin/env python3
"""Listing all documents in a collection"""
import pymongo


def list_all(mongo_collection):
    """Listing all documents in a collection"""
    all = mongo_collection.find()
    return all if all.count() > 0 else []
