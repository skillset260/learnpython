import pymongo
from bson.objectid import ObjectId
from datetime import datetime

# --- MongoDB Configuration ---
# Update the connection string if you are using MongoDB Atlas
client = pymongo.MongoClient("mongodb://cdtmongodb:se4r3svsdf@103.99.36.222/digifyclinic?authSource=admin")
db = client["digifyclinic"]
collection = db["investigations"]

# --- Constants from your Sample ---
ORG_ID = "69a6ab7f78007284396be982"
ORG_NAME = "DummyTestOrg"
CREATED_AT = datetime(2026, 2, 12, 12, 0, 45, 501000)

investigation_records = []

for i in range(1, 201):
    # Generating unique hex suffixes for 24-char ObjectIds
    suffix = str(i).zfill(3)
    # unique_id = f"69a6b05878007284396fa{suffix}"
    
    record = {
        # "_id": ObjectId(unique_id),
        "organizationId": ObjectId(ORG_ID),
        "organizationName": ORG_NAME,
        "investigationName": f"Investigation - {i} (High fever)",
        "description": "It helps your body by identifying underlying causes",
        "isDeleted": False,
        "isActive": True,
        "createdAt": CREATED_AT,
        "updatedAt": CREATED_AT,
        "__v": 0
    }
    investigation_records.append(record)

# --- Execute Bulk Insert ---
try:
    print(f"Starting bulk insert of {len(investigation_records)} records...")
    result = collection.insert_many(investigation_records)
    print(f"Successfully inserted {len(result.inserted_ids)} records into '{collection.name}'.")
except Exception as e:
    print(f"An error occurred during insertion: {e}")
finally:
    client.close()