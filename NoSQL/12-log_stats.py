#!/usr/bin/env python3
"""
module 12-log_stats
"""

from pymongo import MongoClient


def main():
    """
    Connects to the local MongoDB databases
        and display infos for the nginx collection in the logs database.

    Infos displayed:
    - Counts the total number of logs
    - Counts the number of logs per HTTP method (GET, POST, PUT, PATCH, DELETE)
    - Counts the number of status checks (GET requests with the path "/status")

    Raises:
        Exception: If an error occur
    """
    try:
        client = MongoClient('mongodb://localhost:27017/')
        client.server_info()
        db = client['logs']
        collection = db['nginx']
        if collection is not None:
            total_logs = collection.count_documents({})
            print(f"{total_logs} logs")

            print("Methods:")
            for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
                count = collection.count_documents({"method": method})
                print(f"\tmethod {method}: {count}")

            status_check = collection.count_documents({"method": "GET",
                                                       "path": "/status"})
            print(f"{status_check} status check")
    except Exception as e:
        print(f"Error cannot process: {e}")


if __name__ == "__main__":
    """
    not execution solo, module only
    """
    main()
