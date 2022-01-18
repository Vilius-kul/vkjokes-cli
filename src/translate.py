from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import LanguageTranslatorV3

from .settings import TRANSLATION_API_KEY, TRANSLATION_URL


class Translator:

    authenticator = IAMAuthenticator(TRANSLATION_API_KEY)
    language_translator = LanguageTranslatorV3(
        version="2018-05-01", authenticator=authenticator
    )

    @classmethod
    def watson_translate(cls, joke, lang_input):  # type: ignore

        # Authentication
        cls.language_translator.set_service_url(TRANSLATION_URL)
        # translation via ibm_watson api
        translation = cls.language_translator.translate(text=joke, source="en", target=lang_input).get_result()  # type: ignore
        # from dict to str + new line after each joke
        string = ""
        for j in translation["translations"]:  # type: ignore
            string += j["translation"]  # type: ignore
        return string

    # mock translator
    # @staticmethod
    # def translate(text: str, language: str) -> str:
    #     jstring = "".join([j for j in text])

    #     return f"{jstring} Selected language to translate to: {language}"
