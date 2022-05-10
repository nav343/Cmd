import requests
import json

req = requests.get('https://api.dictionaryapi.dev/api/v2/entries/en/home')
req_data = json.loads(req.text)
word = req_data

print(word)
