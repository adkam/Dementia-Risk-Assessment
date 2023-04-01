from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from assessment.api import Assessment

app = Flask(__name__)
api = Api(app)
CORS(app)

api.add_resource(Assessment, '/assessment')

if __name__ == '__main__':
    app.run(debug=True)