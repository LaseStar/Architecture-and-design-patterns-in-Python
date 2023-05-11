from wsgiref.simple_server import make_server

from lase_framework.main import Framework
from urls import routes, fronts

application = Framework(routes, fronts)

with make_server('', 8090, application) as httpd:
    print("Запуск на порту 8090...")
    httpd.serve_forever()
