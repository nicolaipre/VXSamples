from future.plugins import Plugin
import requests
import os


class VirusTotalPlugin(Plugin):
    def __init__(self):
        self.lol = "lol"

    def lookup(self, hash: str):
        api_key = os.getenv("VIRUSTOTAL_API_KEY")
        url = f"https://www.virustotal.com/api/v3/files/{hash}"
        response = requests.get(url, headers={"x-apikey": api_key})
        return response.json()

# https://www.virustotal.com/gui/file/631b8003b56f1381af44cf157d7c08aaa8f958909a3feab4f1b245eeca7427a1
