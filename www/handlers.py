from coroweb import get, post

@get('/')
def index(request):
    return b'<h1>Awesome</h1>'
