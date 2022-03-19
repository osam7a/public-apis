import requests
import aiohttp

base_url = 'https://cleanuri.com/api/v1'

def shorten(self, long):
    resp = requests.get(f'{base_url}/shorten?long={long}')
    return resp.json()['result_url']

async def shorten(self, long):
    async with aiohttp.ClientSession() as cs:
        async with cs.get(f"{base_url}/shorten?long={long}") as resp:
            _json = await resp.json() 
            return _json['result_url']