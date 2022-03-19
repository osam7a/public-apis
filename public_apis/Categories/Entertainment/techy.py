import aiohttp
import requests 
import asyncio 

def techy():
    resp = requests.get('https://techy-api.vercel.app/api/json')
    _json = resp.json()
    return _json['message']

async def async_techy():
    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://techy-api.vercel.app/api/json') as resp:
            _json = await resp.json()
            return _json['message']


if __name__ == '__main__':
    print(techy())