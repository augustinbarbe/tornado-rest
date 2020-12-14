import tornado.web
from tornado.options import options

from sumo_result.apis import api

settings = {
    # debug: If True the application runs in debug mode
    "debug": True,
    # gzip: If True, responses in textual formats will be gzipped automatically.
    "gzip": True,
}

def create_app():
    app = tornado.web.Application(**settings)
    api.init_app(app)
    return app