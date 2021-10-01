import requests

class Switch:
    
    base_url = 'http://127.0.0.1:5000/'
    
    @classmethod
    def input_switch(cls, count, lang):
        if count == 1 and lang == '':
            endpoint = 'random-joke'
            url = cls.base_url+endpoint
            r = requests.get(url)
            return r.text
        if count > 1 and lang == '':
            endpoint = 'multi-random-jokes'
            url = cls.base_url + endpoint
            payload = {'count': count}
            r = requests.get(url, params=payload)
            return r.text
        if lang != '':
            endpoint = 'multi-language-jokes'
            url = cls.base_url + endpoint
            payload = {'count': count,'language':lang}
            r = requests.get(url, params=payload)
            return r.text