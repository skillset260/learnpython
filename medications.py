import pymongo
from bson.objectid import ObjectId
from datetime import datetime

# --- MongoDB Connection ---
# Update with your actual connection string (e.g., MongoDB Atlas URI)
client = pymongo.MongoClient("mongodb://cdtmongodb:se4r3svsdf@103.99.36.222/digifyclinic?authSource=admin")
db = client["digifyclinic"]
collection = db["medications"]

# --- Constants from your Sample ---
ORG_ID = "69a6ab7f78007284396be982"
ORG_NAME = "DummyTestOrg"
CREATED_AT = datetime(2026, 2, 24, 9, 47, 10, 610000)

medication_records = []

# Common dosage forms to rotate through for variety
dosage_forms = ["CAPSULE", "TABLET", "SYRUP", "INJECTION"]

for i in range(1, 201):
    # Unique hex suffix for the 24-character ObjectId
    suffix = str(i).zfill(3)
    # unique_id = f"69a6b05878007284396aa{suffix}"
    
    record = {
        # "_id": ObjectId(unique_id),
        "organizationId": ObjectId(ORG_ID),
        "organizationName": ORG_NAME,
        "name": f"Paracetamol {i}",
        "brandName": "cipla",
        "genericName": "cipla",
        "strength": "650mg",
        "dosageForm": dosage_forms[i % len(dosage_forms)],
        "route": "ORAL",
        "isControlledDrug": True,
        "notes": "Standard medication notes for clinical use.",
        "isDeleted": False,
        "isActive": True,
        "createdAt": CREATED_AT,
        "updatedAt": CREATED_AT,
        "__v": 0
    }
    medication_records.append(record)

# --- Bulk Insertion ---
try:
    print(f"Preparing to insert {len(medication_records)} medications...")
    result = collection.insert_many(medication_records)
    print(f"Successfully inserted {len(result.inserted_ids)} records into '{collection.name}'.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    client.close()