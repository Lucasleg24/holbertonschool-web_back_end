#!/usr/bin/env python3

"""
module 11-schools_by_topic
"""


def schools_by_topic(mongo_collection, topic):
    """
      Returns a list of schools that have the given topic in their topics list.

    Args:
        mongo_collection (Collection): The pymongo collection object.
        topic (str): The topic to search for in the 'topics' list.

    Returns:
        list: A list of documents that contain the specified topic in the 'topics' list.
    """

    return list(mongo_collection.find({"topics": topic}))