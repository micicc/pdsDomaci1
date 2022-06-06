import requests
import json

url = "http://localhost:8081/users"

payload = json.dumps({
                "ime": "Mile",
                "prezime": "Milic",
                "username": "milimile",
                "smer": "RN",
                "predmeti": [
                    { "ime" : "MA", "espb" : 8 },
                    { "ime" : "PVI", "espb" : 6 },
                    { "ime" : "ORS", "espb" : 6 }
                ],
                "id": 0
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)