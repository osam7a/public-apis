import requests
import aiohttp

base_url = 'https://cleanuri.com/api/v1'

def shorten(long):
    resp = requests.post(f'{base_url}/shorten', data = {'url': long})
    return resp.json()['result_url']

async def async_shorten(long):
    async with aiohttp.ClientSession() as cs:
        async with cs.post(f'{base_url}/shorten', data = {'url': long}) as resp:
            _json = await resp.json() 
            return _json['result_url']

if __name__ == "__main__":
    print(shorten('https://discord.com'))