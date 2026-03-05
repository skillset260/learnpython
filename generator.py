import csv
import random
import uuid
from datetime import datetime

# Configuration
FILE_NAME = "clinic_data_200.csv"
RECORDS = 200

# Constants from your sample
ORG_ID = "698c1793cd6040a5f05b620f"
ORG_NAME = "krishan"
COUNTRY_ID = "6878f552b7df743e0404717e"
MP_CITIES = [
    ("Indore", "452001"), ("Bhopal", "462001"), ("Gwalior", "474001"), 
    ("Jabalpur", "482001"), ("Ujjain", "456001"), ("Sagar", "470001"),
    ("Ratlam", "457001"), ("Rewa", "486001"), ("Murwas", "464114")
]

header = [
    "_id", "organizationId", "organizationName", "clinicName", "mobile", "email",
    "countryId", "country", "state", "city", "pincode", "addressLine1", 
    "addressType", "isActive", "createdAt", "updatedAt", "mobileWithCode"
]

with open(FILE_NAME, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    
    for i in range(RECORDS):
        city_info = random.choice(MP_CITIES)
        mobile_num = f"{random.randint(7000000000, 9999999999)}"
        
        row = [
            uuid.uuid4().hex[:24], # Simulated MongoDB ObjectId
            ORG_ID,
            ORG_NAME,
            f"{city_info[0].lower()} clinic {i+1}",
            mobile_num,
            f"user_{i}@gmail.com",
            COUNTRY_ID,
            "India",
            "Madhya Pradesh",
            city_info[0],
            city_info[1],
            f"Block - {random.choice(['Lateri', 'Arera', 'Vijay', 'Civil'])} Line {i}",
            "WORK",
            "true",
            "2026-02-13T06:04:18.278Z",
            "2026-03-02T07:39:54.580Z",
            f"+91{mobile_num}"
        ]
        writer.writerow(row)

print(f"Successfully created {FILE_NAME} with 200 records.")