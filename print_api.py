import requests

response = requests.request("GET", "http://localhost:8000/plans/api/")

print(response.json())