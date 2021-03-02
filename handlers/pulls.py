import requests


def get_pulls(state):
    states = ['open', 'closed']
    labels = ['needs work', 'accepted']
    params = {'per_page': '100'}

    if state in states:
        pull = requests.get(f'https://api.github.com/search/issues?q=\
                is:pr+state:{state}+repo:alenaPy/devops_lab', params=params)
    elif state in labels:
        pull = requests.get(f'https://api.github.com/search/issues?q=\
                is:pr+label:"{state}"+repo:alenaPy/devops_lab', params=params)
    elif state is None:
        pull = requests.get(f'https://api.github.com/repos/alenaPy/devops_lab/pulls', params=params)
        return pull.json()
    return pull.json()['items']
