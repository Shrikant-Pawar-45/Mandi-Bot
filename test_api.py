import requests
from datetime import datetime, timedelta

print("Current date:", datetime.now().strftime("%d/%m/%Y"))

API_KEY = "579b464db66ec23bdd000001821e64e87e204b907bc5b548880a106d"
BASE_URL = "https://api.data.gov.in/resource/9ef84268-d588-465a-a308-a864a43d0070"

# Test without filters
params = {"api-key": API_KEY, "format": "json", "limit": "10"}
response = requests.get(BASE_URL, params=params)
print("Status code:", response.status_code)
if response.status_code == 200:
    data = response.json()
    print("Records:", len(data.get("records", [])))
    if data.get("records"):
        print("Sample record:", data["records"][0])
else:
    print("Error:", response.text)

# Test with commodity Onion
params2 = {"api-key": API_KEY, "format": "json", "limit": "100", "filters[commodity]": "Onion"}
response2 = requests.get(BASE_URL, params=params2)
print("\nWith commodity Onion:")
print("Status code:", response2.status_code)
if response2.status_code == 200:
    data2 = response2.json()
    print("Records:", len(data2.get("records", [])))
    if data2.get("records"):
        print("Sample record:", data2["records"][0])
        # Check if any in Maharashtra
        maharashtra_records = [r for r in data2["records"] if r.get('state') == 'Maharashtra']
        print("Maharashtra records:", len(maharashtra_records))
        if maharashtra_records:
            print("Sample Maharashtra:", maharashtra_records[0])
else:
    print("Error:", response2.text)

# Test with date yesterday
yesterday = (datetime.now() - timedelta(days=1)).strftime("%d/%m/%Y")
params3 = {"api-key": API_KEY, "format": "json", "limit": "10", "filters[arrival_date]": yesterday}
response3 = requests.get(BASE_URL, params=params3)
print(f"\nWith date {yesterday}:")
print("Status code:", response3.status_code)
if response3.status_code == 200:
    data3 = response3.json()
    print("Records:", len(data3.get("records", [])))
    if data3.get("records"):
        print("Sample record:", data3["records"][0])
else:
    print("Error:", response3.text)

# Test with commodity and date
params4 = {"api-key": API_KEY, "format": "json", "limit": "100", "filters[commodity]": "Onion", "filters[arrival_date]": "06/10/2025"}
response4 = requests.get(BASE_URL, params=params4)
print("\nWith commodity Onion and date 06/10/2025:")
print("Status code:", response4.status_code)
if response4.status_code == 200:
    data4 = response4.json()
    print("Records:", len(data4.get("records", [])))
    if data4.get("records"):
        print("Sample record:", data4["records"][0])
        maharashtra_records = [r for r in data4["records"] if r.get('state') == 'Maharashtra']
        print("Maharashtra records:", len(maharashtra_records))
        if maharashtra_records:
            print("Sample Maharashtra:", maharashtra_records[0])
else:
    print("Error:", response4.text)
