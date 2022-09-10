import requests


def login(username, password, server_url):
    url = f"{server_url}/api/account/login/{username}+{password}"
    response = requests.get(url).json()
    return response["metadata"]["Gentry's Quest data"]
