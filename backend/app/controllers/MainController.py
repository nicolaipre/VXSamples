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

    def anyrun(request: Request):
        # input_hash = request.
        plugin = plugins["AnyRun"]
        result = plugin.lookup(input_hash)
        response = {"result": result}
        return JSONResponse(response)

    def malshare(request: Request):
        plugin = plugins["MalShare"]
        response = {"result": result}
        return JSONResponse(response)

    def malwarebazaar(request: Request):
        plugin = plugins["MalwareBazaar"]
        response = {"result": result}
        return JSONResponse(response)

    def kaspersky(request: Request):
        plugin = plugins["Kaspersky"]
        response = {"result": result}
        return JSONResponse(response)

    def hybridanalysis(request: Request):
        plugin = plugins["HybridAnalysis"]
        response = {"result": result}
        return JSONResponse(response)

    def triage(request: Request):
        plugin = plugins["Triage"]
        response = {"result": result}
        return JSONResponse(response)

    def metadefender(request: Request):
        plugin = plugins["MetaDefender"]
        response = {"result": result}
        return JSONResponse(response)

    def threatfox(request: Request):
        plugin = plugins["ThreatFox"]
        response = {"result": result}
        return JSONResponse(response)

    def bfk(request: Request):
        plugin = plugins["BFK"]
        response = {"result": result}
        return JSONResponse(response)

    def elfdigest(request: Request):
        plugin = plugins["ELFDigest"]
        response = {"result": result}
        return JSONResponse(response)

    def huntio(request: Request):
        plugin = plugins["HuntIO"]
        response = {"result": result}
        return JSONResponse(response)
