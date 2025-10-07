from future.plugins import Plugin
import requests
import os


# # curl -X GET --header 'Accept: application/json' -u {API_KEY:API_PASSWORD} 'https://exchange.xforce.ibmcloud.com/api/malware/030c5dec24dc8fafff71dc4f0b68ef80b23bd1a276cd76c9530e26ac1e273412'


class IBMXForcePlugin(Plugin):
    def __init__(self):
        self.lol = "lol"

    def lookup(self, hash: str):
        api_key = os.getenv("IBM_XFORCE_API_KEY")
        url = f"https://exchange.xforce.ibmcloud.com/api/malware/{hash}"
        response = requests.get(url, headers={"x-apikey": api_key})
        return response.json()
