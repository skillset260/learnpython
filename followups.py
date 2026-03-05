import pymongo
from bson.objectid import ObjectId
from datetime import datetime, timedelta

# --- MongoDB Connection ---
client = pymongo.MongoClient("mongodb://cdtmongodb:se4r3svsdf@103.99.36.222/digifyclinic?authSource=admin")
db = client["digifyclinic"]
collection = db["followups"]

# --- Constants from your sample ---
ORG_ID = "69a6ab7f78007284396be982"
CLINIC_ID = "69a6d23db34475abe236d85f"
DOCTOR_ID = "69a6c1cce555542012f79b22"
VISIT_ID = "69a6dac3bb5dee01d4b1d022"
PATIENT_ID = "69a6bc23979f138ebc751d13"
FOLLOWUP_BY_ID = "698c1794cd6040a5f05b6211"

CREATED_AT = datetime(2026, 2, 28, 4, 49, 20)
BASE_FOLLOWUP_DATE = datetime(2026, 3, 11, 18, 30, 0)

followup_records = []

for i in range(1, 201):
    suffix = str(i).zfill(3)
    # Unique ID for the follow-up document
    unique_id = f"69a6dac3bb5dee01d4b1d{suffix}"
    
    # Incrementing the followup date by 1 hour for each record to vary the data
    next_date = BASE_FOLLOWUP_DATE + timedelta(hours=i)
    
    record = {
        "_id": ObjectId(unique_id),
        "organizationId": ObjectId(ORG_ID),
        "organizationName": "DummyTestOrg",
        "clinicId": ObjectId(CLINIC_ID),
        "clinicName": "Test Clinic 1",
        "doctorId": ObjectId(DOCTOR_ID),
        "doctorName": "Dr. Chhabra 1",
        "visitId": ObjectId(VISIT_ID),
        "patientId": ObjectId(PATIENT_ID),
        "patientName": "Kunal Jain",
        "mobile": "9297440048",
        "gender": "MALE",
        "dob": "",
        "age": 26,
        "opdNumber": f"OPD-20260220-1771592373470-{suffix}",
        "note": f"Follow-up test note {i}",
        "nextFollowupRequired": True,
        "nextFollowupDate": next_date,
        "status": "DONE",
        "followupById": ObjectId(FOLLOWUP_BY_ID),
        "followupByName": "DummyTestOrg",
        "followupDate": next_date.strftime("%Y-%m-%d"),
        "isDeleted": False,
        "isActive": True,
        "createdAt": CREATED_AT,
        "__v": 0
    }
    followup_records.append(record)

# --- Execute Bulk Insert ---
try:
    print(f"Preparing to insert {len(followup_records)} follow-up records...")
    result = collection.insert_many(followup_records)
    print(f"Successfully inserted {len(result.inserted_ids)} records.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    client.close()