import requests
from urllib.parse import urljoin

class JokeApi:
    
    base_url = "https://v2.jokeapi.dev/joke/"
    
    @classmethod
    def get_random_joke(cls):
        endpoint= "any"
        url = urljoin(cls.base_url, endpoint)
        response = requests.get(url).json()
        joke = ''
        if response["type"] == "twopart":
            joke += f"{response['setup']}... {response['delivery']}"
            # return f"{response['setup']}... {response['delivery']}"
        else:
            joke += response["joke"]
            
        return joke
        
    #Returns 5 random jokes
    @classmethod
    def five_jokes(cls):
        jokes =""
        for j in range(6):
            jokes+=cls.get_random_joke()
        
        return jokes

    #Returns multiple random jokes
    @classmethod
    def multiple_jokes(cls, user_input =0):
        jokes = []
        for j in range(user_input):
            jokes.append(cls.get_random_joke())
        return jokes


