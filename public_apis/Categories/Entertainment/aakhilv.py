import aiohttp
import requests

class Response:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

class Fun:
    def __init__(self):
        self.base_url = 'https://api.aakhilv.me'
        # Aliasing
        self.wyr = self.would_you_rather
        self.async_wyr = self.async_would_you_rather

    def would_you_rather(self, limit = 1):
        if limit > 884:
            raise ValueError('Limit must be 884 or less')
        resp = requests.get(self.base_url + f'/fun/wyr?num={limit}')
        _json = resp.json()
        return _json if len(_json) > 1 else _json[0]

    def fact(self, limit = 1):
        if limit > 350:
            raise ValueError('Limit must be 883504 or less')
        resp = requests.get(self.base_url + f'/fun/facts?num={limit}')
        _json = resp.json()
        return _json if len(_json) > 1 else _json[0]

    async def async_fact(self, limit = 1):
        if limit > 350:
            raise ValueError('Limit must be 350 or less')
        async with aiohttp.ClientSession() as cs:
            async with cs.get(self.base_url + f'/fun/facts?num={limit}') as resp:
                _json = await resp.json()
                return _json if len(_json) > 1 else _json[0]

    async def async_would_you_rather(self, limit = 1):
        if limit > 884:
            raise ValueError('Limit must be 884 or less')
        async with aiohttp.ClientSession() as cs:
            async with cs.get(self.base_url + f'/fun/wyr?num={limit}') as resp:
                _json = await resp.json()
                return _json if len(_json) > 1 else _json[0]

class Bio:
    def __init__(self, limit = 1):
        self.base_url = 'https://api.aakhilv.me'

    def terms(self, limit = 1):
        if limit > 10:
            raise ValueError('Limit must be 10 or less')
        resp = requests.get(self.base_url + f'/bio/terms?num={limit}')
        _json = resp.json()
        if len(_json) > 1:
            result = []
            for i in _json:
                result.append(Response(
                    term = i['term'],
                    definition = i['definition']
                ))
            return result
        else:
            return Response(
                term = _json[0]['term'],
                definition = _json[0]['definition']
            )
    
    async def async_terms(self, limit = 1):
        if limit > 10:
            raise ValueError('Limit must be 10 or less')
        async with aiohttp.ClientSession() as cs:
            async with cs.get(self.base_url + f'/bio/terms?num={limit}') as resp:
                _json = await resp.json()
                if len(_json) > 1:
                    result = []
                    for i in _json:
                        result.append(Response(
                            term = i['term'],
                            definition = i['definition']
                        ))
                    return result
                else:
                    return Response(
                        term = _json[0]['term'],
                        definition = _json[0]['definition']
                    )

if __name__ == '__main__':
    print(Fun().fact(5))
    terms = Bio().terms()
    print("term: " + terms.term + " " + "definition: " + terms.definition)