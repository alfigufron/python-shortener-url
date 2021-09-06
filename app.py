import requests

long_url = input("Input Long URL : ")
if not long_url:
  print("Empty Long URL")
  exit()

# Credential Authentication
username = "o_4lovj8rfbu"
password = "egJ8F-*n7Y=nYab3"


# Log In to Get Access Token
auth_response = requests.post(
  "https://api-ssl.bitly.com/oauth/access_token",
  auth=(username, password)
)
  
if auth_response.status_code == 200:
  access_token = auth_response.content.decode()
else:
  print("Authentication Failed!")
  exit()


# Get GUID to Shortener URL
headers = {"Authorization": f"Bearer {access_token}"}

group_response = requests.get(
  "https://api-ssl.bitly.com/v4/groups",
  headers=headers
)

if group_response.status_code == 200:
  guid = group_response.json()['groups'][0]['guid']
else:
  print("Get Group Failed!")
  exit()


# Request Shorten URL
shorten_response = requests.post(
  "https://api-ssl.bitly.com/v4/shorten",
  json={"group_guid": guid, "long_url": long_url},
  headers=headers
)

if shorten_response.status_code == 200:
  shorten_url = shorten_response.json()['link']
else:
  print("Request Shorten URL Failed!")
  exit()

print(f"Shorten URL : {shorten_url}")