#!/usr/bin/env python3

"""
module 8-all
"""


def list_all(mongo_collection):
    """
    Lists all documents in a MongoDB collection.

    Args:
        mongo_collection (Collection): The pymongo collection object.

    Returns:
        List[dict]: A list of documents in the collection. Returns an empty list if no documents exist.
    """
    return list(mongo_collection.find())
