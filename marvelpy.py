"""
marvelpy is a wrapper around the requests library to facilitate requests to the Marvel Comics API. The calls return requests.Response objects.
"""

import hashlib, random, requests


_base_url = 'http://gateway.marvel.com/v1/public/'
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

    '''
    Custom timestamps disabled for right now since they complicate the
    iterator. Since they can't be used for an iterator without some timestamp
    generator, disable them overall. A timestamp generator is a decent idea
    though and could solve the problem.
    '''
    ts = str(random.randrange(10000))

    assert key is not None
    assert 'public' in key
    assert 'private' in key
    #TODO
    '''
    Better:
    if key is None:
        raise APIKeyError()
    if not ('public' in key and 'private' in key):
        raise APIKeyError()
    '''

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
    Reads a Marvel Comics API public/private key pair from the file file_name. The first line should be the public key, the second line, the private key.
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



def characters(id=None, **kwargs):
    url = _base_url + 'characters' + ('/' + str(id) if id else '')
    return get(url, **kwargs)



def comics(id=None, **kwargs):
    url = _base_url + 'comics' + ('/' + str(id) if id else '')
    return get(url, **kwargs)



def creators(id=None, **kwargs):
    url = _base_url + 'creators' + ('/' + str(id) if id else '')
    return get(url, **kwargs)



def events(id=None, **kwargs):
    url = _base_url + 'events' + ('/' + str(id) if id else '')
    return get(url, **kwargs)



def series(id=None, **kwargs):
    url = _base_url + 'series' + ('/' + str(id) if id else '')
    return get(url, **kwargs)


###


def iterator(f, *args, **kwargs):
    '''
    Works, but Marvel's API doesn't seem to work, at least for the characters endpoint. So exercise caution. Running this to download an entire data set could take a while.
    '''
    params = kwargs.get('params', {})
    params.setdefault('offset', 0)
    params.setdefault('limit', 100)
    kwargs['params'] = params

    r = f(*args, **kwargs)
    if r.status_code != 200:
        r.raise_for_status()
    yield r

    j = r.json()
    total = j['data']['total']
    if total == 0:
        raise StopIteration
    kwargs['params']['offset'] += j['data']['count']

    while kwargs['params']['offset'] < total:
        r = f(*args, **kwargs)
        if r.status_code != 200:
            r.raise_for_status()
        yield r

        j = r.json()
        kwargs['params']['offset'] += j['data']['count']
