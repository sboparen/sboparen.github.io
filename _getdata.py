#!/usr/bin/env python2
import json
import os
import requests

def update_repos():
    response = requests.get('https://api.github.com/users/sboparen/repos')
    response.raise_for_status()
    data = json.loads(response.content)
    keys = ['name', 'description', 'html_url']
    data = [{k: x[k] for k in keys} for x in data]
    data.sort(key=lambda x: x['name'])
    with open('_data/repos.json', 'w') as f:
        f.write(json.dumps(data, indent=4, sort_keys=True))

if __name__ == '__main__':
    os.chdir(os.path.dirname(__file__))
    update_repos()
