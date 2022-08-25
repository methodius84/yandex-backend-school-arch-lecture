from xmlrpc.client import ResponseError
from aiohttp import web
from app.context import AppContext


async def handle(request: web.Request, context: AppContext) -> web.Response:
    return web.json_response({'hello': 'test'})