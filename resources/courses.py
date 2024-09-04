from flask import jsonify
from flask_restful import  Resource
#from flask.ext.restful import Resource

import models

class Courselist(Resource):
    def get(self):
        return jsonify({'courses':[{'title':'Python basics'}]})

class Course(Resource):
    def get(self, id):
        return jsonify({'title':'Python Basics'})
    
    def put(self, id):
        return jsonify({'title':'Python Basics'})
    
    def delete(self, id):
        return jsonify({'title':'Python Basics'})