import base64
import datetime
import logging
import os

import requests


class EdFi():

    def __init__(self, id=None, secret=None, access_token=None):
        if access_token is not None:
            self.access_token = access_token
        elif access_token is None:
            self.id = id
            self.secret = secret
            self.access_token = self._get_access_token()

    def _get_access_token(self):
        """ retrieves access token from ed-fi api """
        credentials_concatenated = ':'.join((self.id, self.secret))
        credentials_encoded = base64.b64encode(credentials_concatenated.encode('utf-8'))
        access_url = os.environ.get('BASE_URL') + '/oauth/token'

        access_headers = {
            'Authorization': b'Basic ' + credentials_encoded
        }

        access_params = {
            'grant_type': 'client_credentials'
        }

        logging.info('Generating new access token...')
        access_response = requests.post(access_url, headers=access_headers, data=access_params)

        if access_response.status_code == 200:
            logging.info('Successfully retrieved new token')
            access_token_json = access_response.json()

            TOKEN_EXPIRATION = datetime.datetime.now() + datetime.timedelta(seconds=access_token_json['expires_in'])

            logging.info(f'Token will expire at {TOKEN_EXPIRATION}')

            return access_token_json['access_token']

        else:
            logging.error(f'Failed to retrieve access token with error {access_response.status_code}')

