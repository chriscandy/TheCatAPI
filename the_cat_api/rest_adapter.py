import requests
import requests.packages
from typing import List, Dict


class RestAdapter:
    """
    Class that handles the REST calls to the Cat API.
    """

    def __init__(self, hostname: str, api_key: str = '', api_version: str = 'v1', ssl_verify: bool = True):
        self.url = "https://{}/{}/".format(hostname, api_version)
        self._api_key = api_key
        self._ssl_verify = ssl_verify
        if not ssl_verify:
            # noinspection PyUnresolvedReferences
            requests.packages.urllib3.disable_warnings()

    def get(self, endpoint: str, api_params: Dict = None) -> List[Dict]:
        """
        Get the data from the Cat API.

        :param endpoint: The endpoint to call.
        :param api_params: The parameters to pass to the endpoint.
        :return The data from the Cat API.
        """
        full_url = self.url + endpoint
        headers = {'x-api-key': self._api_key}
        response = requests.get(full_url, headers=headers, verify=self._ssl_verify, params=api_params)
        data_out = response.json()
        if 200 <= response.status_code < 300:
            return data_out
        raise Exception(data_out['message'])  # Todo: Better error handling

    def post(self, endpoint: str, api_params: Dict = None, data: Dict = None) -> List[Dict]:
        full_url = self.url + endpoint
        headers = {'x-api-key': self._api_key}
        response = requests.post(full_url, headers=headers, verify=self._ssl_verify, params=api_params, json=data)
        data_out = response.json()
        if response >= 200 and response < 300:
            return data_out
        raise Exception(data_out['message'])  # Todo: Better error handling
