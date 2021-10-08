from typing import  List
from src.clients import JokeApi
from src.translate import Translator

class JokeManager:
    
    def __init__(self, joke_count: int, lang: str):
        self.joke_count = joke_count
        self.lang = lang
        
    def fetch_jokes(self) -> List[str]:
        jokes_in_english = JokeApi.multiple_jokes(self.joke_count)
        if self.lang == '':
            return jokes_in_english
        else:
            return [self._translate_joke(joke) for joke in jokes_in_english]
            
        
    # def  fetch_jokes(self) -> List[str]:
    #     jokes_in_english = JokeApi.multiple_jokes(self.joke_count)
    #     return [self._translate_joke(joke) for joke in jokes_in_english]
        
    def _translate_joke(self, joke: str):
        return Translator.watson_translate(joke=joke, lang_input=self.lang)
    

