from flask_restful import Resource,reqparse
from flask_cors import cross_origin
from flask import Flask, request

class Assessment(Resource): 

    @cross_origin(origin='localhost',headers=['Content-Type','Authorization'])
    def post(self):
        response = flask.jsonify({'some': 'data'})
        response.headers.add('Access-Control-Allow-Origin', '*')
        parser = reqparse.RequestParser()
        parser.add_argument('age')
        args = parser.parse_args() 
        return True, 201