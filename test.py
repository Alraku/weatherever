""" import requests

url = "https://d7sms.p.rapidapi.com/secure/send"

payload = {
    "content": "test",
    "from": "XD-Systems",
    "to": 48796289886
}

headers = {
    'content-type': "application/json",
    'authorization': "Basic eWxzczkxNTM6Q3F1ejg2ZEI=",
    'x-rapidapi-host': "d7sms.p.rapidapi.com",
    'x-rapidapi-key': "604ed38143msh8ecaf712c91ac47p131b7ejsn4d8e5f44be58"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text) """