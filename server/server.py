from flask import Flask, request
from flask_restful import Resource, Api

from src import translateEnToDe

app = Flask(__name__)
api = Api(app)

class Translation(Resource):
    def post(self):
        body = request.get_json()
        return {
            'phrase': body["phrase"],
            'translation': translateEnToDe(body["phrase"])
        }

api.add_resource(Translation, '/translate/en-to-de')

if __name__ == "__main__":
    app.run(host="0.0.0.0")