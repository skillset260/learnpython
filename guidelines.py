import pymongo
from bson.objectid import ObjectId
from datetime import datetime

# --- MongoDB Connection ---
# Replace with your actual connection string if using MongoDB Atlas
client = pymongo.MongoClient("mongodb://cdtmongodb:se4r3svsdf@103.99.36.222/digifyclinic?authSource=admin")
db = client["digifyclinic"]
collection = db["guidelines"]

# --- Constants from your Sample ---
ORG_ID = "69a6ab7f78007284396be982"
ORG_NAME = "DummyTestOrg"
CREATED_AT = datetime(2026, 2, 12, 10, 46, 40, 415000)

guideline_records = []

for i in range(1, 201):
    # Unique hex suffix for the 24-character ObjectId
    suffix = str(i).zfill(3)
    # unique_id = f"69a6b0587800728439611{suffix}"
    
    record = {
        # "_id": ObjectId(unique_id),
        "organizationId": ObjectId(ORG_ID),
        "organizationName": ORG_NAME,
        "guidelineName": f"Guideline {i}: Drink 2.5 litres water daily",
        "description": "It helps your body stay hydrated and improves metabolic function.",
        "isDeleted": False,
        "isActive": True,
        "createdAt": CREATED_AT,
        "updatedAt": CREATED_AT,
        "__v": 0
    }
    guideline_records.append(record)

# --- Bulk Insertion ---
try:
    print(f"Preparing to insert {len(guideline_records)} guidelines...")
    result = collection.insert_many(guideline_records)
    print(f"Successfully inserted {len(result.inserted_ids)} records into '{collection.name}'.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    client.close()