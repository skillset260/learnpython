import pymongo
from bson.objectid import ObjectId
from datetime import datetime
import random

# --- MongoDB Connection ---
client = pymongo.MongoClient("mongodb://cdtmongodb:se4r3svsdf@103.99.36.222/digifyclinic?authSource=admin")
db = client["digifyclinic"]
collection = db["visits"]

# --- Fixed IDs from your sample ---
ORG_ID = "69a6ab7f78007284396be982"
CLINIC_ID = "69a6d23db34475abe236d85f"
DOCTOR_ID = "69a6c1cce555542012f79b22"
CREATED_BY_ID = "698b150975876a8930a23740"
oppointment_id = "69a6d89678007284396bec2a"
CREATED_AT = datetime(2026, 2, 24, 9, 28, 31, 504000)

opd_records = []

for i in range(1, 201):
    suffix = str(i).zfill(3)
    # Unique hex suffix for the visit record ID
    # visit_id = f"69a6d89678007284396bf{suffix}"
    # Unique patient ID per visit for testing
    patient_id = f"69a6bc23979f138ebc751{suffix}"
    
    record = {
        # "_id": ObjectId(visit_id),
        "organizationId": ObjectId(ORG_ID),
        "organizationName": "DummyTestOrg",
        "clinicId": ObjectId(CLINIC_ID),
        "clinicName": "Test Clinic 1",
        "doctorId": ObjectId(DOCTOR_ID),
        "doctorName": "Dr. Chhabra 1",
        "patientId": ObjectId(patient_id),
        "patientName": f"Patient Name {i}",
        "mobile": f"9297440{suffix}",
        "gender": random.choice(["MALE", "FEMALE"]),
        "dob": "",
        "age": random.randint(20, 70),
        "appointmentId": ObjectId(oppointment_id), # Linking appointment to the visit
        "opdNumber": f"OPD-20260224-1771925326567-{suffix}",
        "visitType": random.choice(["NEW", "FOLLOW_UP"]),
        "visitStatus": "IN_PROGRESS",
        "notes": "Viral Fever since 1 day",
        "followupDuration": "",
        "nextFollowUpDate": "",
        "createdById": ObjectId(CREATED_BY_ID),
        "createdByName": "Test@asl.com",
        "isActive": True,
        "isDeleted": False,
        "createdAt": CREATED_AT,
        "updatedAt": CREATED_AT,
        "__v": 0
    }
    opd_records.append(record)

# --- Execute Bulk Insert ---
try:
    print(f"Inserting {len(opd_records)} OPD records...")
    result = collection.insert_many(opd_records)
    print(f"Successfully inserted {len(result.inserted_ids)} records.")
except Exception as e:
    print(f"Insertion failed: {e}")
finally:
    client.close()