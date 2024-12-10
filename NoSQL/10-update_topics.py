#!/usr/bin/env python3

"""
moduel 10-update_topics
"""


def update_topics(mongo_collection, name, topics):
    """
    Updates the list of topics for a school document based on the school name

    Args:
        mongo_collection (Collection): The pymongo collection object
        name (str): The name of the school to update
        topics (list of str): The list of topics to set for the school
    """

    mongo_collection.update_many(
        { "name": name },
        { "$set": { "topics": topics } }
    )
