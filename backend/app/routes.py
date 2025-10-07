from app.controllers.MainController import MainController
from future.routing import Get, Post


routes = [

    RouteGroup(
        prefix="/api"
        #subdomain=""
        #middlewares=[]
        routes=[
            Get(path="/virustotal", endpoint=MainController.virustotal, name="VirusTotal Lookup"),
        ]
    )

]
