from urllib.parse import urljoin

import requests


class JokeApi:

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
    def multiple_jokes(cls, user_input: int = 0) -> str:
        jokes = []
        for j in range(user_input):  # type: ignore
            jokes.append(cls.get_random_joke())  # type: ignore
        return jokes  # type: ignore
