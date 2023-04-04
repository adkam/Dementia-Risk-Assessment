from flask import Flask
from flask_restful import Api,Resource,reqparse
from flask_cors import CORS,cross_origin

app = Flask(__name__)
api = Api(app)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', '*')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response

class Assessment(Resource): 
    @cross_origin(origin='localhost',headers=['Content-Type','Authorization'])
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('age')
        args = parser.parse_args() 
        return True, 201

api.add_resource(Assessment, '/assessment')

if __name__ == '__main__':
    app.run(debug=True)