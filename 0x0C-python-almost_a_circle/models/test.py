import requests

response = requests.get('https://requests.sysu.me')

print(response.status_code)
print(response.content)