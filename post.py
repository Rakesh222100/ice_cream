import requests

url = 'https://api.example.com/data'
payload = {'key1': 'value1', 'key2': 'value2'}
response = requests.post(url, json=payload)  # Use json= for JSON payload

if response.status_code == 201:
    data = response.json()  # or response.text for plain text
    print(data)
else:
    print(f"Error: {response.status_code}")

