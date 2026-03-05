import pymongo
from bson.objectid import ObjectId
from datetime import datetime

# 1. Database Configuration
MONGO_URI = "mongodb://cdtmongodb:se4r3svsdf@103.99.36.222/digifyclinic?authSource=admin" 
DB_NAME = "digifyclinic"
COLLECTION_NAME = "treatments"

client = pymongo.MongoClient(MONGO_URI)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]

# 2. Base Data
org_id = "69a6ab7f78007284396be982"
base_time = datetime(2026, 2, 24, 11, 22, 33)

treatment_list = []

# 3. Generate 200 Records
for i in range(1, 201):
    # Creating a unique 24-character hex string for the ID
    unique_suffix = str(i).zfill(3)
       
    record = {
        
        "organizationId": ObjectId(org_id),
        "organizationName": "MotherHood Hospitals",
        "treatmentName": f"Consultation Type {i}",
        "description": "Consult with doctor",
        "isDeleted": False,
        "isActive": True,
        "createdAt": base_time,
        "updatedAt": base_time,
        "__v": 0
    }
    treatment_list.append(record)

# 4. Bulk Insert into MongoDB
try:
    print(f"Preparing to insert {len(treatment_list)} records...")
    result = collection.insert_many(treatment_list)
    print(f"Success! {len(result.inserted_ids)} records inserted into '{COLLECTION_NAME}'.")
except pymongo.errors.BulkWriteError as e:
    print(f"Bulk insert failed. Error details: {e.details}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    client.close()