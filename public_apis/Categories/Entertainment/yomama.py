import requests
import aiohttp

base_url = 'https://yomomma-api.herokuapp.com/jokes'

def joke():
    """ 
    returns a random yomama joke 
    """
    resp = requests.get('https://yomomma-api.herokuapp.com/jokes')
    _json = resp.json() 
    return _json['joke'] 

async def async_joke():
    """ 
    async version of joke()
    """
    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://yomomma-api.herokuapp.com/jokes') as resp:
            _json = await resp.json()
            return _json['joke'] 

if __name__ == '__main__':
    print(joke())
    