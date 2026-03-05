import csv

data = []
for i in range(1, 201):
    mobile = f"9669407{str(i).zfill(3)}"
    data.append({
        "organizationId": "69a6ab7f78007284396be982",
        "organizationName": "DummyTestOrg",
        "clinicName": f"Test Clinic {i}",
        "mobile": mobile,
        "mobileWithCode": f"+91{mobile}",
        "email": f"test{i}@codiotic.com",
        "address.countryId": "6878f552b7df743e0404717e",
        "address.country": "India",
        "address.state": "Madhya Pradesh",
        "address.city": "Indore",
        "address.pincode": "452016",
        "address.addressLine1": "Indore",
        "address.addressLine2": "Dewas",
        "address.addressType": "WORK",
        "isActive": "true",
        "isDeleted": "false",
        "createdAt": "2026-03-03T09:56:40.304Z",
        "updatedAt": "2026-03-03T09:56:40.304Z",
        "__v": 0
    })

with open('dummy_data.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=data[0].keys())
    writer.writeheader()
    writer.writerows(data)

print("Done! Check your folder for dummy_data.csv")