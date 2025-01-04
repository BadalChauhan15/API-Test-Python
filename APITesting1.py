# noinspection PySingleQuotedDocstring
'''
API Testing with Postman or Python (Requests)
Goal: Test an API endpoint that returns a list of users.
Steps:
- Use a public API (e.g., https://jsonplaceholder.typicode.com/users).
- Send a GET request.
- Verify the status code is 200.
- Check the response data structure.
- Print the data in the File.
'''

import json
import requests

# API Endpoint
url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

# Verify status code
assert response.status_code == 200, "Failed: Status code is not 200"

# Verify response structure
data = response.json()
assert isinstance(data, list), "Failed: Response is not a list"

print("API Test Passed")

# File name to store data in JSON format
file_name = "Data.txt"

# Write the JSON data to the file
with open(file_name, 'w') as file:
    # noinspection PyTypeChecker
    json.dump(data, file, indent=4)  # Convert list to JSON and write to file

print(f"Data successfully written in JSON to {file_name}")

# Simplify data for readability
simplified_data = ""
for user in data:
    simplified_data += f"Name: {user['name']}\n"
    simplified_data += f"Username: {user['username']}\n"
    simplified_data += f"Email: {user['email']}\n"
    simplified_data += f"Address Details:\n"
    for key, value in user['address'].items():
        if isinstance(value, dict):  # Handle nested 'geo' dictionary
            simplified_data += f"  {key.capitalize()}:\n"
            for sub_key, sub_value in value.items():
                # Rename keys as needed
                display_key = "Longitude" if sub_key == "lng" else "Latitude" if sub_key == "lat" else sub_key.capitalize()
                simplified_data += f"    {display_key}: {sub_value}\n"
        else:
            simplified_data += f"  {key.capitalize()}: {value}\n"
    simplified_data += f"Phone: {user['phone']}\n"
    simplified_data += f"Website: {user['website']}\n"
    simplified_data += "Company Details:\n"
    for key, value in user['company'].items():
        simplified_data += f"  {key.capitalize()}: {value}\n"
    simplified_data += "-" * 40 + "\n"  # Add a separator for clarity

# File name to save the simplified data
file_name1 = "Data_Info.txt"

# Write the simplified data to the file
with open(file_name1, 'w') as file:
    file.write(simplified_data)

print(f"Simplified Data successfully written to {file_name1}")