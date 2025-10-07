from future.controllers import Controller
from app.settings import plugins


class MainController(Controller):

    def virustotal(request: Request):

        plugin = plugins["VirusTotal"]

        response = {"result": result}
        return JSONResponse(response)
