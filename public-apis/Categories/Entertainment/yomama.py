import requests
import aiohttp

def joke():
    resp = requests.get('https://yomomma-api.herokuapp.com/jokes')
    _json = resp.json() 
    return _json['joke'] 

async def async_joke():
    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://yomomma-api.herokuapp.com/jokes') as resp:
            _json = await resp.json()
            return _json['joke'] 
            