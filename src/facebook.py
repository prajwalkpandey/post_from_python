import json
import sys
import os
import requests

message=sys.argv[1]
page_id=""
page_access_token=""

class Facebook:
    def get(token_name):
        access_token = os.getenv('PWD')+'/access_tokens.txt'
        f = open(access_token, 'r+')
        lines = f.readlines()
        for line in lines:
            tokens = line.strip().split('=')
            if tokens[0] == token_name:
                return tokens[1].strip()
    
    def __init__(self):
        global page_id
        page_id=Facebook.get("Page_ID")
        global page_access_token
        page_access_token=Facebook.get("Access_Token")

    def make_post(self,message):
        url="https://graph.facebook.com/v5.0/"+page_id+"/feed/?message="+message+"&access_token="+page_access_token
        return requests.post(url)


if __name__=="__main__":
    facebook=Facebook()

    response=facebook.make_post(message)

    print(response.json())