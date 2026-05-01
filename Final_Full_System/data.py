from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, ConfigurationError, OperationFailure
import os
from dotenv import load_dotenv


def main():
    try:
        #Load env
        load_dotenv()
        uri = os.getenv("MONGO_URI")

        if not uri:
            raise ValueError("MONGO_URI not found in .env file")

        # Connect to MongoDB
        client = MongoClient(uri, serverSelectionTimeoutMS=5000)

        #Force connection check
        client.admin.command('ping')

        print("Connected to MongoDB successfully")

        # List databases
        databases = client.list_database_names()
        print("\nDatabases:", databases)

        # Loop through DBs and collections
        for db_name in databases:
            try:
                db = client[db_name]
                collections = db.list_collection_names()

                print(f"\n Database: {db_name}")
                print("   Collections:", collections)

            except OperationFailure as e:
                print(f"Cannot access collections in '{db_name}': {e}")

        for db_name in databases:
            try:
                db = client[db_name]
                collections = db.list_collection_names()

                print(f"\nDatabase: {db_name}")
                print("   Collections:", collections)

                for col in collections:
                    print(f"\n Collection: {col}")

                    # Get sample documents (limit 5)
                    docs = list(db[col].find().limit(5))

                    if not docs:
                        print(" No documents found")
                        continue

                    # Extract all keys (fields)
                    fields = set()
                    for doc in docs:
                        fields.update(doc.keys())

                    print(" Fields:", list(fields))

            except OperationFailure as e:
                print(f"Cannot access collections in '{db_name}': {e}")

    except ValueError as e:
        print(f"ENV Error: {e}")

    except ConfigurationError as e:
        print(f"Configuration Error: {e}")

    except ConnectionFailure as e:
        print(f"Connection Failed: {e}")

    except Exception as e:
        print(f"Unexpected Error: {e}")

    finally:
        try:
            client.close()
            print("\nMongoDB connection closed")
        except:
            pass


if __name__ == "__main__":
    main()