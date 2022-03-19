import requests
import aiohttp

class Response:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)
        

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
        elif resp.status_code == 200 or resp.status_code == 201:
            _json = resp.json()
            deeplinks = []
            for i in _json['deeplinks']:
                deeplinks.append(Response(
                    guid=i['guid'],
                    bitlink = i['bitlink']
                    app_uri_path = i['app_uri_path'],
                    install_url = i['install_url'],
                    app_guid = i['app_guid'],
                    os = i['os'],
                    install_type = i['install_type']
                    created = i['created'],
                    modified = i['modified'],
                    brand_guid = i['brand_guid']
                ))
            return Response(
                references = _json['references'],
                link = _json['link'],
                id = _json['id'],
                long_url = json['long_url'],
                archived = json['archived'],
                created_at = json['created_at'],
                custom_bitlinks = _json['custom_bitlinks'],
                tags = _json['tags']
                deeplinks = deeplinks
            )
        elif resp.status_code in [400, 422, 429, 417, 503, 500]:
            _json = resp.json()
            return Response(
                message = _json['message'],
                description = _json['description'],
                resource = _json['resource'],
                errors = [Response(i['field'], i['error_code'], i['message']) for i in _json['errors']]
            )

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
                elif resp.status_code == 200 or resp.status_code == 201:
                    _json = await resp.json()
                    return Response(
                        references = _json['references'],
                        link = _json['link'],
                        id = _json['id'],
                        long_url = json['long_url'],
                        archived = json['archived'],
                        created_at = json['created_at'],
                        custom_bitlinks = _json['custom_bitlinks'],
                        tags = _json['tags']
                        deeplinks = [Response(
                            guid=i['guid'],
                            bitlink = i['bitlink']
                            app_uri_path = i['app_uri_path'],
                            install_url = i['install_url'],
                            app_guid = i['app_guid'],
                            os = i['os'],
                            install_type = i['install_type']
                            created = i['created'],
                            modified = i['modified'],
                            brand_guid = i['brand_guid']
                        ) for i in _json['deeplinks']]
                    )
                elif resp.status_code in [400, 422, 429, 417, 503, 500]:
                    _json = resp.json()
                    return Response(
                        message = _json['message'],
                        description = _json['description'],
                        resource = _json['resource'],
                        errors = [Response(i['field'], i['error_code'], i['message']) for i in _json['errors']]
                    )

    