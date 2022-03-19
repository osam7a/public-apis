import requests
import aiohttp

class Bitly:
    def __init__(self, auth):
        self.auth = auth
        self.base_url = 'https://api-ssl.bitly.com/v4'

    def shortenURL(self, long, groupguid, domain = None):
        data = {
            "long_url": long,
            "group_guid": groupguid,
        }
        if domain: data['domain'] = domain
        headers = {
            "Authorization": self.auth,
            "Content-Type": "application/json"
        }
        resp = requests.post(self.base_url + '/shorten', headers=headers, data=data)
        if resp.status_code == 403:
            raise ValueError("Invalid Auth Token")
        elif resp.status_code == 429:
            raise TimeoutError("Too Many Requests")

    async def shortenURL(self, long, groupguid, domain = None):
        data = {
            "long_url": long,
            "group_guid": groupguid,
        }
        if domain: data['domain'] = domain
        headers = {
            "Authorization": self.auth,
            "Content-Type": "application/json"
        }
        async with aiohttp.ClientSession() as cs:
            async with cs.get(self.base_url + '/shorten', headers=headers, data=data) as resp:
                if resp.status_code == 403:
                    raise ValueError("Invalid Auth Token")
                elif resp.status_code == 429:
                    raise TimeoutError("Too Many Requests")

    