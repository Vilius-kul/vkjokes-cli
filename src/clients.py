from urllib.parse import urljoin

import requests


class JokeApi:
    """Class responsible for calling external API as well as setting joke filters, returning joke or jokes"""

    base_url = "https://v2.jokeapi.dev/joke/"

    @classmethod
    def get_random_joke(cls):
        endpoint = "Any?blacklistFlags=nsfw,racist,sexist,explicit"
        url = urljoin(cls.base_url, endpoint)
        response = requests.get(url).json()
        joke = ""
        if response["type"] == "twopart":
            joke += f"{response['setup']}... {response['delivery']}"
        else:
            joke += response["joke"]

        return joke

    # Returns multiple random jokes
    @classmethod
    def multiple_jokes(cls, user_input=0):
        jokes = []
        for j in range(user_input):
            jokes.append(cls.get_random_joke())
        return jokes
