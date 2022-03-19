import aiohttp
import requests

class Response:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

base_url = 'http://namo-memes.herokuapp.com'

def random(limit = 1):
    resp = requests.get(base_url + f'/memes/{limit}')
    _json = resp.json()
    if limit == 1:
        return Response(
            id = _json['_id'],
            url = _json['url'],
            created_at = _json['createdAt'],
            updated_at = _json['updatedAt']
        )
    else:
        result = []
        for i in _json:
            result.append(Response(
            id = i['_id'],
            url = i['url'],
            created_at = i['createdAt'],
            updated_at = i['updatedAt']
        ))
        return result

async def async_random(limit = 1):
    async with aiohttp.ClientSession() as cs:
        async with cs.get(f"{base_url}/memes/{limit}") as resp:
            _json = await resp.json()
            if limit == 1:
                return Response(
                    id = _json['_id'],
                    url = _json['url'],
                    created_at = _json['createdAt'],
                    updated_at = _json['updatedAt']
                )
            else:
                result = []
                for i in _json:
                    result.append(Response(
                    id = i['_id'],
                    url = i['url'],
                    created_at = i['createdAt'],
                    updated_at = i['updatedAt']
                ))
                return result

def latest(limit = 1):
    resp = requests.get(base_url + f'/memes/latest/{limit}')
    _json = resp.json()
    if limit == 1:
        return Response(
            id = _json[0]['_id'],
            url = _json[0]['url'],
            created_at = _json[0]['createdAt'],
            updated_at = _json[0]['updatedAt']
        )
    else:
        result = []
        for i in _json:
            result.append(Response(
            id = i['_id'],
            url = i['url'],
            created_at = i['createdAt'],
            updated_at = i['updatedAt']
        ))
        return result

async def async_latest(limit = 1):
    async with aiohttp.ClientSession() as cs:
        async with cs.get(f"{base_url}/memes/latest/{limit}") as resp:
            _json = await resp.json()
            if limit == 1:
                return Response(
                    id = _json['_id'],
                    url = _json['url'],
                    created_at = _json['createdAt'],
                    updated_at = _json['updatedAt']
                )
            else:
                result = []
                for i in _json:
                    result.append(Response(
                    id = i['_id'],
                    url = i['url'],
                    created_at = i['createdAt'],
                    updated_at = i['updatedAt']
                ))
                return result

if __name__ == '__main__':
    print(latest().url)