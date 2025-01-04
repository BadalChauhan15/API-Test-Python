# noinspection PySingleQuotedDocstring
'''
Performance Testing with Python
Goal: Measure the response time of an API.
'''

import requests
import time

# API Endpoint
url = "https://jsonplaceholder.typicode.com/posts"

# Measure response time
start_time = time.time()
response = requests.get(url)
end_time = time.time()

# Verify status code and log time
assert response.status_code == 200, "Failed: Status code is not 200"
print(f"Response Time: {end_time - start_time} seconds")