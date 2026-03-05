import json

records = []
for i in range(1, 201):
    suffix = str(i).zfill(3)
    mobile = f"9669407{suffix}"
    
    obj = {
        "organizationId": "69a6ab7f78007284396be982",
        "organizationName": "DummyTestOrg",
        "clinicName": f"Test Clinic {i}",
        "mobile": mobile,
        "mobileWithCode": f"+91{mobile}",
        "email": f"test{i}@codiotic.com",
        "address": {
            "countryId": "6878f552b7df743e0404717e",
            "country": "India",
            "state": "Madhya Pradesh",
            "city": "Indore",
            "pincode": "452016",
            "addressLine1": "Indore",
            "addressLine2": "Dewas",
            "landmark": "",
            "addressType": "WORK",
            "isActive": True,
            "_id": f"69a6b05878007284396beb{suffix}",
            "createdAt": "2026-03-03T09:56:40.304Z",
            "updatedAt": "2026-03-03T09:56:40.304Z"
        },
        "isDeleted": False,
        "isActive": True,
        "createdAt": "2026-03-03T09:56:40.304Z",
        "updatedAt": "2026-03-03T09:56:40.304Z",
        "__v": 0
    }
    records.append(obj)

# Wrap in "data" key as requested
final_json = {"data": records}

with open('data.json', 'w') as f:
    json.dump(final_json, f, indent=4)

print("Created data.json with 200 records successfully!")