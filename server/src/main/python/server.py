from flask import Flask, request
from flask_restful import Resource, Api
from prometheus_client import Gauge
from random import *
from werkzeug.wsgi import DispatcherMiddleware
from prometheus_client import make_wsgi_app


def getCurrentTemperature() :
    temp = randint(0,30)
    print (temp)
    return temp


class Ping(Resource) : 
    def get(self):
        return "Pong";

class Temperature(Resource): 
    def get(self, label, temp) :
        g.labels(label).set(temp)
        return

class Hygrometrie(Resource):
    def get(self, label, hyg) :
        g2.labels(label).set(hyg)
        return


app = Flask(__name__)
api = Api(app)

g = Gauge('current_temp', 'Temperature actuelle', ['sensor'])
#g.set_to_current_time()
#g.labels('i').inc()

g2 = Gauge('current_hygro', 'Hygrometrie actuelle', ['sensor'])
#g2.set_to_current_time()
#g2.labels('A').inc()

api.add_resource(Ping, "/ping")
api.add_resource(Temperature, "/temperature/<label>/<temp>")
api.add_resource(Hygrometrie, "/hygrometrie/<label>/<hyg>")


app_dispatch = DispatcherMiddleware(app, {
    '/metrics': make_wsgi_app()
})


#if __name__ == '__main__':
#     app.run(port='5000')

