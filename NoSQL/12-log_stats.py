#!/usr/bin/env python3
"""
module 12-log_stats.py
"""


from pymongo import MongoClient


def main():
    """
    use MongoClient for collect data info of db
    stock logs, stock nginx and check data
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
