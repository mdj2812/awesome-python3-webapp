import logging; logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime

from aiohttp import web

routes = web.RouteTableDef()

@routes.get('/')
async def index(request):
    return web.Response(body=b'<h1>Awesome</h1>', headers={'content-type':'text/html'})

def init():
    app = web.Application()
    app.router.add_routes(routes)
    logging.info('Server started at http://127.0.0.1:9000...')
    web.run_app(app, host='127.0.0.1', port=9000)

init()