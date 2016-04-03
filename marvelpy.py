"""
MarvelPy is a wrapper around the requests library to facilitate requests to the Marvel Comics API. The calls return requests.Response objects.
"""

import functools, hashlib, random, requests


_base_url = 'http://gateway.marvel.com/v1/public/'


### Classes ###


class Keychain:
    def __init__(self):
        self.index = None
        self.keychain = []


    def add_key(self, key):
        self.keychain.append(key)

        if self.index is None:
            self.index = 0


    def key(self):
        return None if self.index is None else self.keychain[self.index]
    

    def next_key(self):
        if self.index is None or self.index + 1 == len(self.keychain):
            return None

        self.index += 1
        return self.keychain[self.index]


keychain = Keychain()


### Exceptions ###


class APIKeyError(Exception):
    pass


###


def _build_headers(kwargs):
    headers = dict(kwargs.get('headers', {}))
    kwargs['headers'] = headers

    etag = kwargs.pop('etag', None)
    if etag:
        headers['If-None-Match'] = etag



def _build_params(kwargs):
    #ts
    params = dict(kwargs.get('params', {}))
    kwargs['params'] = params

    key = keychain.key()

    if key is None:
        raise APIKeyError('Keychain empty.')
    if not ('public' in key and 'private' in key):
        raise APIKeyError('API key has no public or private key.')

    ts = kwargs.pop('ts', str(random.randrange(10000)))

    m = hashlib.md5()
    m.update(ts.encode())
    m.update(key['private'].encode())
    m.update(key['public'].encode())
    
    params['ts'] = ts
    params['apikey'] = key['public']
    params['hash'] = m.hexdigest()



def load_keys(file_name):
    num_keys = 0

    with open(file_name) as f:
        for line in f:
            if line.endswith('\n'):
                line = line[:-1]

            key = {}
            try:
                key['public'], key['private'] = line.split(',')
            except ValueError:
                raise APIKeyError('Invalid API key file format.')

            num_keys += 1
            keychain.add_key(key)
    
    return num_keys


'''
def set_default_key(k):
    global _default_key
    _default_key = k
'''


### Level 1


#Special keyword arguments: etag, session, ts
def get(url, **kwargs):
    _build_params(kwargs)
    _build_headers(kwargs)

    s = kwargs.pop('session', requests)
    return s.get(url, **kwargs)



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


### Level 2


def _get_response(g, tries):
    tries -= 1
    r = g()

    # 401 is probably the response for too many API calls, but maybe not
    while r.status_code == 401 or (r.status_code == 500 and tries > 0):
        if r.status_code == 401:
            if keychain.next_key() is None:
                break
        else: # 500
            tries -= 1

        r = g()

    # At this point, we've done all we can
    return r


def iterator(f, *args, tries=1, **kwargs):
    #For now, ignore customs timestamps and etags for iterators
    kwargs.pop('etag', None)
    kwargs.pop('ts', None)

    params = dict(kwargs.get('params', {}))
    kwargs['params'] = params
    params.setdefault('offset', 0)
    params.setdefault('limit', 100)

    g = functools.partial(f, *args, **kwargs)

    r = _get_response(g, tries)
    yield r

    if r.status_code != 200:
        raise StopIteration

    j = r.json()
    total = j['data']['total']
    if total == 0:
        raise StopIteration
    kwargs['params']['offset'] += j['data']['count']

    while kwargs['params']['offset'] < total:
        r = _get_response(g, tries)
        yield r

        if r.status_code != 200:
            raise StopIteration

        kwargs['params']['offset'] += r.json()['data']['count']


### Level 3 ###


def get_all(f, *args, tries=1, filter=None, **kwargs):
    results = []
    for r in iterator(f, *args, tries=tries, **kwargs):
        if r.status_code != 200:
            break

        j = r.json()
        if j['data']['count'] > 0:
            for i in j['data']['results']:
                if filter:
                    entry = {}
                    for attribute in filter:
                        entry[attribute] = i[attribute]
                    results.append(entry)
                else:
                    results.append(i)

    return results, r


### Test Objects


class TestGet:
    def __init__(self, n):
        self.n = n

    def __call__(self, url, **kwargs):
        if self.n:
            return TestResponse(self.n.pop(0), 1000, url, **kwargs)
        
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


        
