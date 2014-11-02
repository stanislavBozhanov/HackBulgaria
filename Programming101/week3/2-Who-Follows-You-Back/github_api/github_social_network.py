import requests


class GitHubSocialNetwork():
    def __init__(self):
        self.json = None
    def get_json(self):
        f = open('token.txt', 'r')
        token = f.read()
        f.close()
        username = 'stanislav.bozhanov@gmail.com'
        r = requests.get()
          