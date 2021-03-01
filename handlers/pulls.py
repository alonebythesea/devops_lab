import requests


def get_pulls(state):
    owner = 'alenaPy'
    repo = 'devops_lab'
    states = ['open', 'closed']

    req_accepted = requests.get(f'http://api.github.com/search/issues?q=is:pr+ \
            label:accepted+repo:{owner}/{repo}')
    req_needs_work = requests.get(f'http://api.github.com/search/issues?q=is:pr+ \
            label:"needs work"+repo:{owner}/{repo}')
    req_pull_states = requests.get(f'http://api.github.com/search/issues?q=is:pr+ \
            state:{state}+repo:{owner}/{repo}')
    req_pulls = requests.get(f'https://api.github.com/repos/alenaPy/devops_lab/pulls')

    if state in states:
        pull = req_pull_states.json()
    elif state == 'accepted':
        pull = req_accepted.json()
    elif state == 'needs work':
        pull = req_needs_work.json()
    else:
        pull = req_pulls.json()
    return pull if not state else pull['items']
