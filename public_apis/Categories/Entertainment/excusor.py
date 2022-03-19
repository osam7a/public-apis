import aiohttp 
import requests 

class Response:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

class Excusor:
    def __init__(self):
        self.base_url = "https://excuser.herokuapp.com/v1/excuse"
        self.categories = ['family', 'office', 'children', 'college', 'party']

    def random(self, limit = None):
        resp = requests.get(f"{self.base_url}{f'/{limit}' if limit is not None else ''}")
        _json = resp.json()
        if len(_json) > 1:
            result = []
            for i in _json:
                result.append(Response(
                    id = i['id'],
                    excuse = i['excuse'],
                    category = i['category']
                ))
            return result
        else:
            return Response(
                id = _json[0]['id'],
                excuse = _json[0]['excuse'],
                category = _json[0]['category']
            )

    async def async_random(self, limit = None):
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"{self.base_url}{f'/{limit}' if limit is not None else ''}") as resp:
                _json = await resp.json()
                if len(_json) > 1:
                    result = []
                    for i in _json:
                        result.append(Response(
                            id = i['id'],
                            excuse = i['excuse'],
                            category = i['category']
                        ))
                    return result
                else:
                    return Response(
                        id = _json[0]['id'],
                        excuse = _json[0]['excuse'],
                        category = _json[0]['category']
                    )
    
    def random_category(self, category, limit = None):
        if category.lower() not in self.categories:
            raise AttributeError("Category not found... Check the categories attribute of this class")
        resp = requests.get(f"{self.base_url}/{category}{f'/{limit}' if limit is not None else ''}")
        _json = resp.json()
        if len(_json) > 1:
            result = []
            for i in _json:
                result.append(Response(
                    id = i['id'],
                    excuse = i['excuse'],
                    category = i['category']
                ))
            return result
        else:
            return Response(
                id = _json[0]['id'],
                excuse = _json[0]['excuse'],
                category = _json[0]['category']
            )

    async def async_random_category(self, category, limit = None):
        if category.lower() not in self.categories:
            raise AttributeError("Category not found... Check the categories attribute of this class")
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"{self.base_url}/{category}{f'/{limit}' if limit is not None else ''}") as resp:
                _json = await resp.json()
                if len(_json) > 1:
                    result = []
                    for i in _json:
                        result.append(Response(
                            id = i['id'],
                            excuse = i['excuse'],
                            category = i['category']
                        ))
                    return result
                else:
                    return Response(
                        id = _json[0]['id'],
                        excuse = _json[0]['excuse'],
                        category = _json[0]['category']
                    )

if __name__ == '__main__':
    excusor = Excusor()
    print(excusor.random().execuse)
    print([i.excuse for i in excusor.random(limit = 5)]) 