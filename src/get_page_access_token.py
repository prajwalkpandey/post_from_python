import json
import requests
import sys

user_access_token=sys.argv[1]

response=requests.get("https://graph.facebook.com/me/accounts?access_token="+user_access_token)

dic=response.json()

for page in dic["data"]:
    print("Page Name: "+page["name"])
    print("Page ID: "+page["id"])
    print("Page Access Token: "+page["access_token"])
