import pymongo
from bson.objectid import ObjectId
from datetime import datetime
import random

# --- Connection Setup ---
# Update the URI if you are using MongoDB Atlas
client = pymongo.MongoClient("mongodb://cdtmongodb:se4r3svsdf@103.99.36.222/digifyclinic?authSource=admin")
db = client["digifyclinic"]
collection = db["complaints"]

# --- Base Data ---
org_id = "69a6ab7f78007284396be982"
org_name = "DummyTestOrg"
created_at = datetime(2026, 2, 12, 8, 2, 53)

# List of names to make the 200 records varied
names = ["Fever", "Cough", "Fatigue", "Headache", "Nausea", "Chills", "Body Ache"]

records = []

for i in range(1, 201):
    suffix = str(i).zfill(3)
    # Creating a unique 24-character hex ID
    # unique_id = f"69a6b05878007284396da{suffix}"
    
    # Pick a name and append the index for uniqueness
    condition_name = f"{random.choice(names)} Type {i}"
    
    record = {
       
        "organizationId": ObjectId(org_id),
        "organizationName": org_name,
        "name": condition_name,
        "bodySystem": "GENERAL",
        "description": "Elevated body temperature or related general symptom",
        "isDeleted": False,
        "isActive": True,
        "createdAt": created_at,
        "updatedAt": created_at,
        "__v": 0
    }
    records.append(record)

# --- One-Time Bulk Insertion ---
try:
    print(f"Attempting to insert {len(records)} records...")
    result = collection.insert_many(records)
    print(f"Success! {len(result.inserted_ids)} records added to the database.")
except Exception as e:
    print(f"Error during insertion: {e}")
finally:
    client.close()