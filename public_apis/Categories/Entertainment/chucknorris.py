import aiohttp
import requests

class Response:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)


class ChuckNorris:
    def __init__(self):
        self.base_url = 'https://api.chucknorris.io/jokes'

    def random(self, category = None):
        """
        Gets a random chucknorris joke
        Parameters: category = None
        Returns: Response object with attributes: created_at, categories, icon_url, id, rawJson, url, value
        """

        resp = requests.get(f"{self.base_url}/random{f'?category={category}' if category is not None else ''}")
        _json = resp.json()
        return Response(
              created_at=_json['created_at'],
              categories=_json['categories'],
              icon_url = _json['icon_url'],
              id = _json['id'],
              rawJson = _json,
              url = _json['url'],
              value = _json['value']
        )
    
    def search(self, query):
        """ 
        Search through chucknorris jokes 
        Parameters: query: str 
        Returns list of Response(created_at, categories, icon_url, id, rawJson, url, value)
        """

        resp = requests.get(f"{self.base_url}/search?query={query}")
        _json = resp.json()
        results = []
        for i in _json['result']:
            results.append(Response(
                created_at=i['created_at'],
                categories=i['categories'],
                icon_url = i['icon_url'],
                id = i['id'],
                rawJson = i,
                url = i['url'],
                value = i['value']
            ))
        return Response(
            found = _json['total'],
            results = results
        )

    async def async_search(self, query):

        """ 
        async version of search()
        """

        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"{self.base_url}/search?query={query}") as resp:
                _json = await resp.json()
                results = []
                for i in _json['result']:
                    results.append(Response(
                        created_at=i['created_at'],
                        categories=i['categories'],
                        icon_url = i['icon_url'],
                        id = i['id'],
                        rawJson = i,
                        url = i['url'],
                        value = i['value']
                    ))
                return Response(
                    found = _json['total'],
                    results = results
                )


    @property 
    def categories(self):
        resp = requests.get(f"{self.base_url}/categories")
        return resp.json()

    async def async_random(self, category = None):
        """ 
        The async version of random()
        """

        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"{self.base_url}/random{f'?category={category}' if category is not None else ''}") as resp:
                _json = await resp.json()
                return Response(
                    created_at=_json['created_at'],
                    categories=_json['categories'],
                    icon_url = _json['icon_url'],
                    id = _json['id'],
                    rawJson = _json,
                    url = _json['url'],
                    value = _json['value']
                )

if __name__ == '__main__':
    chuck = ChuckNorris()
    print(chuck.random().value)
    print(chuck.categories)
    print(chuck.search("chuck norris").found)