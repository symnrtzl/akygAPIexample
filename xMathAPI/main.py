import requests

response = requests.get("https://x-math.herokuapp.com/api/add")

print(response.json())
