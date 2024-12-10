#!/usr/bin/env python3

"""
module 9-insert_school
"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a MongoDB collection based on keyword arguments.

    Args:
        mongo_collection (Collection): The pymongo collection object.
        **kwargs: Key-value pairs to be inserted as a document.

    Returns:
        str: The ID of the newly inserted document.
    """

    result = mongo_collection.insert_one(kwargs)
    return str(result.inserted_id)
