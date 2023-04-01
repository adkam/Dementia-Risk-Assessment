from flask_restful import Resource,reqparse

class Assessment(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('age')
        args = parser.parse_args()
        return True, 201