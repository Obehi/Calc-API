from flask import Flask, abort
from flask_restful import Api, Resource, reqparse
import engine as engine

app = Flask(__name__)
api = Api(app)


# Calculates expression and returns result
class Calc(Resource):
    def post(self):
        
        parser = reqparse.RequestParser()
        parser.add_argument('expression', type=str, required=True)
        args = parser.parse_args()
        
        return  engine.calc_json_expression(args['expression'])

# Returns a list of calc history from old to new
class History(Resource):
    def get(self):
        return  engine.get_history()


api.add_resource(Calc, "/calc/")
api.add_resource(History, "/history/")

app.run(debug=True)