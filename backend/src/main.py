from flask import Flask
from flask_restful import Api,Resource,reqparse
from flask_cors import CORS,cross_origin

app = Flask(__name__)
api = Api(app)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

class Assessment(Resource): 
    @cross_origin()
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('age')
        args = parser.parse_args() 
        return True, 201

api.add_resource(Assessment, '/assessment')

if __name__ == '__main__':
    app.run(debug=True)