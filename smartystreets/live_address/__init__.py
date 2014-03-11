import requests
import ujson


class Geocoder(object):

    AUTH_ID = None
    AUTH_TOKEN = None
    ENDPOINT = 'https://api.smartystreets.com/street-address'

    def __init__(self, AUTH_ID=None, AUTH_TOKEN=None):
        if AUTH_ID:
            self.AUTH_ID = AUTH_ID
        if AUTH_TOKEN:
            self.AUTH_TOKEN = AUTH_TOKEN

    def batch(self, *locations, **kwargs):

        if not self.AUTH_ID:
            raise Exception("AUTH_ID has not been set!")
        if not self.AUTH_TOKEN:
            raise Exception("AUTH_TOKEN has not been set!")

        final_endpoint = '%s?auth-id=%s&auth-token=%s' % (self.ENDPOINT,
                                                          self.AUTH_ID,
                                                          self.AUTH_TOKEN)

        data = locations
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        r = requests.post(final_endpoint,
                          data=ujson.dumps(data),
                          headers=headers)

        return [{'input_index': item['input_index'],
                 'longitude': item['metadata']['longitude'],
                 'latitude': item['metadata']['latitude']} for item in r.json()]
