import requests
import json
headers = {'Authorization': 'Token YOUR_TOKEN'}
username = 'YOUR_USERNAME'
response = requests.get(f'https://api.github.com/users/{username}/repos', headers=headers)
repositories = json.loads(response.text)
for repository in repositories:
    print(f'{repository["full_name"]}: {repository["description"]}')
