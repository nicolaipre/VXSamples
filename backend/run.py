from future.application import Future
from app.settings import config, lifespan
from app.routes import routes
from rich import print


app = Future(lifespan=lifespan, config=config)
app.add_routes(routes=routes)
# print(app.routes)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000, workers=1)  # , access_log=True)
