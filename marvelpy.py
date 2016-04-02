"""
marvelpy is a wrapper around the requests library to facilitate requests to the Marvel Comics API. The calls return requests.Response objects.
"""

import hashlib, random, requests


_base_url = 'http://gateway.marvel.com/v1/public/'
_default_key = None



class APIKeyError(Exception):
    pass



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

    if key is None:
        raise APIKeyError('No default key set and no key provided.')
    if not ('public' in key and 'private' in key):
        raise APIKeyError('API key has no public or private key.')

    m = hashlib.md5()
    m.update(ts.encode())
    m.update(key['private'].encode())
    m.update(key['public'].encode())
    
    params['ts'] = ts
    params['apikey'] = key['public']
    params['hash'] = m.hexdigest()

    return params



def load_key(file_name, default=False):
    """
    Reads a Marvel Comics API public/private key pair from the file file_name. The first line should be the public key, the second line, the private key.
    """
    with open(file_name) as f:
        key = {}
        s = f.readline()
        if s.endswith('\n'):
            s = s[:-1]
        key['public'], key['private'] = s.split(',')

    if default:
        set_default_key(key)
    
    return key


def set_default_key(k):
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


def iterator(f, *args, tries=1, **kwargs):
    params = kwargs.setdefault('params', {})
    params.setdefault('offset', 0)
    params.setdefault('limit', 100)

    r = f(*args, **kwargs)
    retries = tries - 1
    while r.status_code == 500 and retries:
        retries -= 1
        r = f(*args, **kwargs)
    yield r

    if r.status_code != 200:
        raise StopIteration

    j = r.json()
    total = j['data']['total']
    if total == 0:
        raise StopIteration
    kwargs['params']['offset'] += j['data']['count']

    while kwargs['params']['offset'] < total:
        r = f(*args, **kwargs)
        retries = tries - 1
        while r.status_code == 500 and retries:
            retries -= 1
            r = f(*args, **kwargs)
        yield r

        if r.status_code != 200:
            raise StopIteration

        kwargs['params']['offset'] += r.json()['data']['count']


### Test Objects


class TestGet:
    def __init__(self, n):
        self.n = n

    def __call__(self, url, **kwargs):
        if self.n:
            self.n -= 1
            return TestResponse(500, 1000, url, **kwargs)
        
        return TestResponse(200, 1000, url, **kwargs)



class TestResponse:
    def __init__(self, status_code, total, *args, **kwargs):
        self.status_code = status_code
        self.j = {}
        self.j['data'] = {}
        self.j['data']['total'] = total
        self.j['data']['offset'] = kwargs['params']['offset']
        self.j['data']['count'] = kwargs['params']['limit']

    def json(self):
        return self.j


        
