import requests


url = "https://api.pipefy.com/graphql"

headers = {
    "Accept": "application/json",
    "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJ1c2VyIjp7ImlkIjozMDEzMDc5NTgsImVtYWlsIjoiaG91c3Rvbi5zYW50b3NAdmVjdHJhY3MuY29tLmJyIiwiYXBwbGljYXRpb24iOjMwMDEwNzEzNn19.COu8S2Eh8jKOLWlBJrxJ-ddNAexoDT8BBlHGtxQ-cnv5qWuvBR0AjuDNOAHVcCdKpfCUrc5kRDGJIjKx6RcL5A",
    "Content-Type": "application/json"
}


payload = {"query": "{me{name, email}}"}

response = requests.request("POST", url, json = payload, headers = headers)

print(response.text)