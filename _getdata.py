#!/usr/bin/env python2
import json
import os
import requests

categories = [
    ('My Everyday Software', [
        'env',
        'dwm',
        'gmail-snooze',
        'ren',
        ]),
    ('Projects', [
        '1k-codec',
        'vrdemo',
        ]),
    ('Video Game Related', [
        'openitg',
        'spacechem',
        'stepmania',
        'tis100',
        ]),
    ('Source Code For This Website', [
        'sboparen.github.io',
        'resume',
        ]),
]

def update_repos():
    response = requests.get('https://api.github.com/users/sboparen/repos')
    response.raise_for_status()
    data = json.loads(response.content)
    data = {repo['name']: repo for repo in data}
    output = []
    for title, reponames in categories:
        repos = []
        for reponame in reponames:
            assert reponame in data, '%s not found' % reponame
            repo = data[reponame]
            del data[reponame]
            keys = ['name', 'description', 'html_url']
            if repo['description'].startswith('https://sboparen.github.io/'):
                repo['description'] = ''
            repos.append({k: repo[k] for k in keys})
        output.append({'title': title, 'repos': repos})
    assert len(data) == 0, 'uncategorized repos: %s' % data.keys()
    with open('_data/repos.json', 'w') as f:
        f.write(json.dumps(output, indent=4, sort_keys=True))

if __name__ == '__main__':
    os.chdir(os.path.dirname(__file__))
    update_repos()
