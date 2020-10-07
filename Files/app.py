import requests
import sys

username = "o_5tn54cki0a"
password = "Can6269eml$"

auth_res = requests.post("https://api-ssl.bitly.com/oauth/access_token", auth=(username, password))
if auth_res.status_code == 200:
    access_token = auth_res.content.decode()
    print('[!] Got access token: ', access_token)
else:
    print('[!] Cannot get access token, exiting...')
    exit()

headers = {"Authorization": f"Bearer {access_token}"}

group_res = requests.get("https://api-ssl.bitly.com/v4/groups", headers=headers)
if group_res.status_code == 200:
    groups_data = group_res.json()['groups'][0]
    guid = groups_data['guid']
else:
    print('[!] Cannot get GUID, exiting...')
    exit()

url = sys.argv[1]
shorten_res = requests.post("https://api-ssl.bitly.com/v4/shorten", json={"group_guid": guid, "long_url": url}, headers=headers)
if shorten_res.status_code == 200:
    link = shorten_res.json().get("link")
    print("Shortened URL:", link)
else:
    print("[!] Error with URL, exiting...")
    exit()
