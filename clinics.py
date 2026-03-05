import pymongo
from bson.objectid import ObjectId
from datetime import datetime

# 1. Connect to MongoDB
# Replace with your actual connection string
client = pymongo.MongoClient("mongodb://cdtmongodb:se4r3svsdf@103.99.36.222/digifyclinic?authSource=admin")
db = client["digifyclinic"]
collection = db["clinics"]

records = []
base_org_id = "69a6ab7f78007284396be982"

for i in range(1, 201):
    # Creating unique suffixes to avoid duplicate key errors
    suffix = str(i).zfill(3)
    
    # We use ObjectId() to ensure MongoDB treats these as IDs, not strings
   
    addr_id = f"69a6b05878007284396bc{suffix}"
    mobile = f"9669407{suffix}"
    
    record = {
       
        "organizationId": ObjectId(base_org_id),
        "organizationName": "DummyTestOrg",
        "clinicName": f"Test Clinic {i}",
        "mobile": mobile,
        "mobileWithCode": f"+91{mobile}",
        "email": f"test{i}@codiotic.com",
        "address": {
            "countryId": ObjectId("6878f552b7df743e0404717e"),
            "country": "India",
            "state": "Madhya Pradesh",
            "city": "Indore",
            "pincode": "452016",
            "addressLine1": "Indore",
            "addressLine2": "Dewas",
            "landmark": "",
            "addressType": "WORK",
            "isActive": True,
            "_id": ObjectId(addr_id),
            "createdAt": datetime(2026, 3, 3, 9, 56, 40),
            "updatedAt": datetime(2026, 3, 3, 9, 56, 40)
        },
        "isDeleted": False,
        "isActive": True,
        "createdAt": datetime(2026, 3, 3, 9, 56, 40),
        "updatedAt": datetime(2026, 3, 3, 9, 56, 40),
        "__v": 0
    }
    records.append(record)

# 2. Insert all 200 records at once
try:
    result = collection.insert_many(records)
    print(f"Successfully inserted {len(result.inserted_ids)} records!")
except Exception as e:
    print(f"An error occurred: {e}")