import asyncio

from aiohttp import web

routes = web.RouteTableDef()


@routes.get('/')
async def index(request):
    await asyncio.sleep(0.5)
    return web.Response(body=b'<h1>Index</h1>', content_type='text/html')


@routes.get('/hello/{name}')
async def hello(request):
    await asyncio.sleep(0.5)
    text = '<h1>Hello, %s!</h1>' % request.match_info['name']
    return web.Response(body=text.encode('utf-8'), content_type='text/html')


app = web.Application()
app.add_routes(routes)
web.run_app(app, host='localhost', port=8000)