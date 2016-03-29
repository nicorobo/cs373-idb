"""
marvelpy is a wrapper around the requests library to facilitate requests to the Marvel Comics API. The calls return requests.Response objects.
"""

import hashlib, random, requests


_base_url = 'http://gateway.marvel.com{}'
_default_key = None


def _build_headers(etag=None, **kwargs):
    headers = {}
    if etag:
        headers['If-None-Match'] = etag

    return headers



def _build_params(params=None, key=None, ts=None, **kwargs):
    if not params:
        params = {}
    if not key:
        key = _default_key
    if not ts:
        ts = str(random.randrange(10000))

    m = hashlib.md5()
    m.update(ts.encode())
    m.update(key['private'].encode())
    m.update(key['public'].encode())
    
    params['ts'] = ts
    params['apikey'] = key['public']
    params['hash'] = m.hexdigest()

    return params



def read_key(file_name, default=False):
    """
    Reads a Marvel API public/private key pair from the file file_name. The first line should be the public key, the second line, the private key.
    """
    with open(file_name) as f:
        key = {}
        key['public'] = f.readline()[:-1]
        key['private'] = f.readline()

    if default:
        set_key(key)
    
    return key


def set_key(k):
    global _default_key
    _default_key = k


###



def get(url, **kwargs):
    kwargs['params'] = _build_params(**kwargs)
    kwargs['headers'] = _build_headers(**kwargs)

    s = kwargs.pop('session', None)
    if s:
        return s.get(url, **kwargs)

    return requests.get(url, **kwargs)



def character(character_id, **kwargs):
    url = _base_url.format('/v1/public/characters/{}').format(character_id)
    return get(url, **kwargs)



def characters(**kwargs):
    url = _base_url.format('/v1/public/characters')
    return get(url, **kwargs)



def comic(comic_id, **kwargs):
    url = _base_url.format('/v1/public/comics/{}').format(comic_id)
    return get(url, **kwargs)



def comics(**kwargs):
    url = _base_url.format('/v1/public/comics')
    return get(url, **kwargs)



def creator(creator_id, **kwargs):
    url = _base_url.format('/v1/public/creators/{}').format(creator_id)
    return get(url, **kwargs)



def creators(**kwargs):
    url = _base_url.format('/v1/public/creators')
    return get(url, **kwargs)



def event(event_id, **kwargs):
    url = _base_url.format('/v1/public/events/{}').format(event_id)
    return get(url, **kwargs)



def events(**kwargs):
    url = _base_url.format('/v1/public/events')
    return get(url, **kwargs)


# Stupid name because series is both singular and plural
def single_series(series_id, **kwargs):
    url = _base_url.format('/v1/public/series/{}').format(series_id)
    return get(url, **kwargs)



def series(**kwargs):
    url = _base_url.format('/v1/public/series')
    return get(url, **kwargs)
