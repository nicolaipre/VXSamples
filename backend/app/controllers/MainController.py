from future.controllers import Controller
from future.requests import Request
from future.responses import JSONResponse
from app.settings import plugins


class MainController(Controller):
    async def lookup(request: Request):
        # plugin = plugins["VirusTotal"]
        # response = {"result": result}
        input_hash = "0dea6f77da9bdfd6985c3cd30c6c174d791d106ce55dd5f57a2f212ab5477c67"
        response = {
            f"hash": f"{input_hash}",
            "matches": [
                {
                    "source": "VirusTotal",
                    "downloadable": True,
                    "filename": "malware.exe",
                    "detectionRate": "45/70",
                    "url": f"https://www.virustotal.com/gui/file/{input_hash}/detection"
                }
            ]
        }
        return JSONResponse(response)
