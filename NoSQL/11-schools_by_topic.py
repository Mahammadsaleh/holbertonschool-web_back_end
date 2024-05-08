#!/usr/bin/env python3
"""Documentation"""


def schools_by_topic(mongo_collection, topic):
    return [collection for collection in mongo_collection.find(
        {"topics": topic}
        )]
