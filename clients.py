from src.clients import JokeApi
from src.translate import Translator


class JokeManager:
    """Class, decision maker... Deciding if translator is needed"""

    def __init__(self, joke_count, lang):
        self.joke_count = joke_count
        self.lang = lang

    def fetch_jokes(self):
        jokes_in_english = JokeApi.multiple_jokes(self.joke_count)
        if not self.lang:
            return jokes_in_english
        else:
            return [self._translate_joke(joke) for joke in jokes_in_english]

    def _translate_joke(self, joke):
        return Translator.watson_translate(joke=joke, lang_input=self.lang)
