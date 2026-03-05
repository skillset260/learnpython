import pymongo
from bson.objectid import ObjectId
from datetime import datetime

# --- Database Connection ---
client = pymongo.MongoClient("mongodb://cdtmongodb:se4r3svsdf@103.99.36.222/digifyclinic?authSource=admin")
db = client["digifyclinic"]
collection = db["diagnoses"]

# --- Constants ---
ORG_ID = "69a6ab7f78007284396be982"
ORG_NAME = "DummyTestOrg"
CREATED_AT = datetime(2026, 2, 16, 9, 6, 21)
UPDATED_AT = datetime(2026, 2, 16, 9, 15, 7)

records = []

# List of medical categories to rotate through
categories = ["INFECTIOUS", "NEOPLASMS", "ENDOCRINE", "NERVOUS", "RESPIRATORY"]

for i in range(1, 201):
    suffix = str(i).zfill(3)
    # Unique 24-character hex ID for MongoDB
    # unique_id = f"6990063b09ff988ec1afc{suffix}"
    
    # Generate unique ICD code and Category
    icd_code = f"A20{suffix}"
    category_name = categories[i % len(categories)]
    
    record = {
        # "_id": ObjectId(unique_id),
        "organizationId": ObjectId(ORG_ID),
        "organizationName": ORG_NAME,
        "name": f"Diagnosis Test {i}",
        "icdCode": icd_code,
        "category": category_name,
        "description": "Standard medical diagnosis description for ICD classification.",
        "isDeleted": False,
        "isActive": True,
        "createdAt": CREATED_AT,
        "updatedAt": UPDATED_AT,
        "__v": 0
    }
    records.append(record)

# --- One-Time Bulk Insertion ---
try:
    print(f"Preparing to insert {len(records)} records...")
    result = collection.insert_many(records)
    print(f"Successfully inserted {len(result.inserted_ids)} records into '{collection.name}'.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    client.close()