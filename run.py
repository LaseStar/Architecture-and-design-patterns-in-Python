from wsgiref.simple_server import make_server

from lase_framework.main import Framework
from urls import fronts
from views import routes

application = Framework(routes, fronts)

with make_server('', 8030, application) as httpd:
    print("Запуск на порту 8030...")
    httpd.serve_forever()
