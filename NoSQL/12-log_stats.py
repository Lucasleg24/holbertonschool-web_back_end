#!/usr/bin/env python3
"""
module 12-log_stats
"""

from pymongo import MongoClient

def main():
    """
    Use MongoClient to collect data info of db, stock logs, stock nginx, and check data
    """
    try:
        # Connexion au serveur MongoDB
        client = MongoClient('mongodb://localhost:27017/')

        # Vérifie si la base de données 'logs' existe
        databases = client.list_database_names()
        if 'logs' not in databases:
            raise Exception("La base de données 'logs' n'existe pas.")

        # Accède à la base de données 'logs'
        db = client['logs']

        # Vérifie si la collection 'nginx' existe dans la base de données
        collections = db.list_collection_names()
        if 'nginx' not in collections:
            raise Exception("La collection 'nginx' n'existe pas dans la base de données 'logs'.")

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
        status_check = collection.count_documents({"method": "GET", "path": "/status"})
        print(f"{status_check} status check")

    except Exception as e:
        print(f"Erreur : {e}")

if __name__ == "__main__":
    """
    Exécution du module principal
    """
    main()
