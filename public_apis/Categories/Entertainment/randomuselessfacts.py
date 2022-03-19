import aiohttp
import requests

class Response:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

class RandomUselessFacts:
    def __init__(self):
        self.base_url = 'https://uselessfacts.jsph.pl'

    def random(self, language='en'):
        resp = requests.get(self.base_url + f'/random.json?language={language}')
        _json = resp.json()
        return Response(
            id = _json['id'],
            text = _json['text'],
            source = _json['source'],
            source_url = _json['source_url'],
            language = _json['language'],
            permalink = _json['permalink']
        )

    def today(self, language='en'):
        resp = requests.get(self.base_url + f'/today.json?language={language}')
        _json = resp.json()
        return Response(
            id = _json['id'],
            text = _json['text'],
            source = _json['source'],
            source_url = _json['source_url'],
            language = _json['language'],
            permalink = _json['permalink']
        )

    async def async_random(self, language='en'):
        async with aiohttp.ClientSession() as cs:
            async with cs.get(self.base_url + f'/random.json?language={language}') as resp:
                _json = await resp.json()
                return Response(
                    id = _json['id'],
                    text = _json['text'],
                    source = _json['source'],
                    source_url = _json['source_url'],
                    language = _json['language'],
                    permalink = _json['permalink']
                )

    async def async_today(self, language='en'):
        async with aiohttp.ClientSession() as cs:
            async with cs.get(self.base_url + f'/daily.json?language={language}') as resp:
                _json = await resp.json()
                return Response(
                    id = _json['id'],
                    text = _json['text'],
                    source = _json['source'],
                    source_url = _json['source_url'],
                    language = _json['language'],
                    permalink = _json['permalink']
                )

if __name__ == '__main__':
    print(RandomUselessFacts().today().text)
    print(RandomUselessFacts().random().text)