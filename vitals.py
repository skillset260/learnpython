import pymongo
from bson.objectid import ObjectId
from datetime import datetime

# --- MongoDB Connection ---
# Replace the URI with your connection string if using Atlas
client = pymongo.MongoClient("mongodb://cdtmongodb:se4r3svsdf@103.99.36.222/digifyclinic?authSource=admin")
db = client["digifyclinic"]
collection = db["vitals"]

# --- Constants ---
ORG_ID = "69a6ab7f78007284396be982"
ORG_NAME = "DummyTestOrg"
CREATED_AT = datetime(2026, 2, 11, 8, 6, 39)

records = []

for i in range(1, 201):
    # Unique identifiers for each record
    suffix = str(i).zfill(3)
    # main_id = f"69a6b05878007284396ea{suffix}"
    range_id = f"69a6b05878007284396eb{suffix}"
    
    record = {
        # "_id": ObjectId(main_id),
        "organizationId": ObjectId(ORG_ID),
        "organizationName": ORG_NAME,
        "name": f"Blood Pressure Test {i}",
        "code": f"BP{suffix}",
        "unit": "mmHg",
        "isNumeric": True,
        "ageWiseNormalRanges": [
            {
                "_id": ObjectId(range_id),
                "minAge": 20,
                "maxAge": 40,
                "minValue": 90,
                "maxValue": 110,
                "gender": "FEMALE",
                "description": f"Standard range for group {i}",
                "isDeleted": False,
                "isActive": True,
                "createdAt": CREATED_AT,
                "updatedAt": CREATED_AT
            }
        ],
        "isDeleted": False,
        "isActive": True,
        "createdAt": CREATED_AT,
        "updatedAt": CREATED_AT,
        "__v": 0
    }
    records.append(record)

# --- Execute Bulk Insert ---
try:
    print(f"Starting bulk insert of {len(records)} records...")
    result = collection.insert_many(records)
    print(f"Successfully inserted {len(result.inserted_ids)} health metrics.")
except Exception as e:
    print(f"An error occurred during insertion: {e}")
finally:
    client.close()