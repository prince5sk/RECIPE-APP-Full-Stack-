from flask import request
from flask_api import status
from flask_restx import Resource

from ..util.dto import UserDto
from app.main.service.user_service import *

api = UserDto.api
_user = UserDto.user


@api.route('/')
class UserList(Resource):
    @api.doc('list of registered users')
    @api.marshal_list_with(_user, envelope="data")
    def get(self):
        """ List of registered users """
        return get_all_users()

    @api.response(status.HTTP_201_CREATED, 'User registered successfully')
    @api.doc('create a new user')
    @api.expect(_user, validate=True)
    def post(self):
        """ Creates a new User """
        data = request.json
        return save_new_user(data=data)


@api.route('/<public_id>/')
@api.param('public_id', 'The User identifier')
@api.response(status.HTTP_404_NOT_FOUND, 'User not found')
class User(Resource):
    @api.doc('get a user')
    @api.marshal_with(_user)
    def get(self, public_id):
        """ get a user given its identifier """
        user = get_a_user(public_id)
        if not user:
            api.abort(status.HTTP_404_NOT_FOUND)
        else:
            return user
    
    @api.doc('delete a user')
    def delete(self, public_id):
        """ delete a user given its identifier """
        user = get_a_user(public_id)
        if not user:
            api.abort(status.HTTP_404_NOT_FOUND)
        else:
            delete_user(user)
