from future.controllers import Controller
from app.settings import plugins


class MainController(Controller):

    def virustotal(request: Request):

        plugin = plugins["VirusTotal"]

        response = {"result": result}
        return JSONResponse(response)

    def anyrun(request: Request):

        plugin = plugins["AnyRun"]

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

