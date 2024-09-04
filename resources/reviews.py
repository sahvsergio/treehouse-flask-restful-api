from flask import jsonify
from flask_restful import Resource
# from flask.ext.restful import Resource

import models


class Reviewlist(Resource):
    def get(self):
        return jsonify({'reviews    ': [{'course':1, 'rating':5}]})


class Review(Resource):
    def get(self, id):
        return jsonify({'course': 1, 'rating': 5})

    def put(self, id):
        return jsonify({'course': 1, 'rating': 5})

    def delete(self, id):
        return jsonify({'course': 1, 'rating': 5})
