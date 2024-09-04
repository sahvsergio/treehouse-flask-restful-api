from flask import jsonify, Blueprint
from flask_restful import  Resource, Api
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



courses_api=Blueprint('courses',__name__)
api=Api(courses_api)
api.add_resource(Courselist, '/api/v1/courses', endpoint='courses')
api.add_resource(Course, '/api/v1/courses/<int:id>', endpoint='course')