import pymongo
from bson.objectid import ObjectId
from datetime import datetime

# --- Configuration ---
MONGO_URI = "mongodb://cdtmongodb:se4r3svsdf@103.99.36.222/digifyclinic?authSource=admin" # Change if using MongoDB Atlas
DB_NAME = "digifyclinic"
COLLECTION_NAME = "doctors"

client = pymongo.MongoClient(MONGO_URI)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]

# Base Data
org_id = "69a6ab7f78007284396be982"
base_created_at = datetime(2026, 3, 3, 9, 30, 31)

doctor_records = []

for i in range(1, 201):
    # Generating unique hex suffixes for ObjectIds (24 chars total)
    suffix = str(i).zfill(3)
   
    
    # Simulating unique mobile numbers starting from your base
    # 9479879100, 9479879101, etc.
    mobile_num = str(9479879100 + i)

    record = {
        
        "organizationId": ObjectId(org_id),
        "organizationName": "codiotic",
        "doctorName": f"Dr. Chhabra {i}",
        "mobile": mobile_num,
        "specialization": "skin, hair",
        "qualification": "test",
        "experienceYears": 10,
        "isDeleted": False,
        "isActive": True,
        "createdAt": base_created_at,
        "updatedAt": base_created_at,
        "__v": 0
    }
    doctor_records.append(record)

# --- Execute Bulk Insert ---
try:
    print(f"Starting insert of {len(doctor_records)} records...")
    result = collection.insert_many(doctor_records)
    print(f"Successfully inserted {len(result.inserted_ids)} doctors into '{COLLECTION_NAME}'.")
except pymongo.errors.BulkWriteError as e:
    print(f"Bulk insert failed. Check for duplicate IDs. Error: {e.details}")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    client.close()