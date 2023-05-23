import requests
import json
username = input("Enter a Github username: ")
url = "https://api.github.com/users/" + username + "/repos"
response = requests.get(url)
data = json.loads(response.text)

for i in data:
    print(i["name"])
