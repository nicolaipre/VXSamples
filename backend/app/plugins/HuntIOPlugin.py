from future.plugins import Plugin
import requests

# https://apidocs.hunt.io/reference/attackcapture-download-zip-file


class HuntIOPlugin(Plugin):
    def __init__(self):
        pass

    def lookup(self, hash: str):
        url = "https://api.hunt.io/v1/attackcapture/download-zip-file"
        headers = {"accept": "application/json"}
        response = requests.get(url, headers=headers)
        print(response.text)
