from wsgiref.simple_server import make_server

from lase_framework.main import Framework
from urls import routes, fronts


application = Framework(routes, fronts)

with make_server('', 8040, application) as httpd:
    print("Запуск на порту 8040...")
    httpd.serve_forever()
