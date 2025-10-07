from app.controllers.MainController import MainController
from future.routing import Get, Post, RouteGroup


routes = [

    RouteGroup(
        prefix="/api",
        # subdomain=""
        # middlewares=[]
        routes=[
            Get(path="/lookup", endpoint=MainController.lookup,
                name="VirusTotal Lookup"),
        ]
    )

]
