import requests
import json

url = 'https://cataas.com/cat?json=true'

res = requests.get(url)
data = json.loads(res.text)

name = data['url']

print(res.text)
print()
print()
print()
print(data)
print()
print(name)
