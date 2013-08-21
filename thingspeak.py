import httplib, urllib

field_keys = ['field' + str(n) for n in xrange(1,9)]
headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}

def non_null_values(**kwargs):
    return [(k,v) for (k,v) in kwargs.iteritems() if v != None]

class TooManyFields(ValueError):
    pass

class channel(object):
    def __init__(self, key):
        self.key = key

    def update(self, field_vals, lat=None, long=None, elevation=None, status=None):
        if len(vals) > 8:
            raise TooManyFields('update can only handle 8 field values per channel')
        # this verbosity, rather than just using kwargs,
        # so that callers get a prompt error if they supply an arg `update` cannot handle
        named_args = non_null_values(lat=lat, long=long, elevation=elevation, status=status)
        params = urllib.urlencode(zip(field_keys, vals) + [('key', self.key)] + named_args)
        conn = httplib.HTTPConnection("api.thingspeak.com:80")
        conn.request("POST", "/update", params, headers)
        response = conn.getresponse()
        conn.close()
        return response