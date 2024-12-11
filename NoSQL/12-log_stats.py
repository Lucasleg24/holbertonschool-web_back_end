#!/usr/bin/env python3
"""
module 12-log_stats
"""


from pymongo import MongoClient


def main():
    """
    Use MongoClient to collect data info of db, stock logs,
    stock nginx, and check data
    """
    try:
        # Connexion au serveur MongoDB
        client = MongoClient('mongodb://localhost:27017/')

        # Accède à la base de données 'logs'
        db = client['logs']

        # Accède à la collection 'nginx'
        collection = db['nginx']

        # Compte le nombre total de documents dans la collection
        total_logs = collection.count_documents({})
        print(f"{total_logs} logs")

        # Affiche les statistiques des méthodes HTTP
        print("Methods:")
        for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
            count = collection.count_documents({"method": method})
            print(f"\tmethod {method}: {count}")

        # Compte les vérifications de statut
        status_check = collection.count_documents({"method": "GET",
                                                   "path": "/status"})
        print(f"{status_check} status check")

    except Exception as e:
        print(f"Error : {e}")


if __name__ == "__main__":
    """
    Exécution du module principal
    """
    main()
