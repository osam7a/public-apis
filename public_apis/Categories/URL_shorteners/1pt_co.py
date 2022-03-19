import aiohttp
import requests

class Response:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

def addURL(long, short = None):
    resp = requests.get(f"api.1pt.co?long={long}{f'&short={short}' if short else ''}")
    _json = resp.json()
    try:
        return Response(
            status = _json['status'],
            message = _json['message'],
            short = _json['short'],
            long = _json['long']
        )
    except: return _json