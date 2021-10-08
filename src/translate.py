from .settings import TRANSLATION_API_KEY,TRANSLATION_URL
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

class Translator:

    authenticator = IAMAuthenticator(TRANSLATION_API_KEY)
    language_translator = LanguageTranslatorV3(version='2018-05-01',
                                           authenticator=authenticator)       

    @classmethod
    def watson_translate(cls,joke, lang_input):
        
        #Authentication 
        cls.language_translator.set_service_url(TRANSLATION_URL)
        #translation via ibm_watson api
        translation = cls.language_translator.translate(text=joke,source='en',target=lang_input).get_result()
        #from dict to str + new line after each joke
        string =''
        for j in translation['translations']:
            string += j['translation']
        return string

    #mock translator
    @staticmethod
    def translate(text: str, language: str) -> str:
        jstring =''.join([j for j in text])

        return f"{jstring} Selected language to translate to: {language}"