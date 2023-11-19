import uuid
import datetime

from flask_api import status

from app.main import db
from app.main.model.user import User


def save_new_user(data):
    user = User.query.filter_by(email=data['email']).first()
    if not user:
        new_user = User(
            public_id=str(uuid.uuid4()),
            email=data['email'],
            # username=data['username'],
            username=data['email'].split('@')[0],
            password=data['password'],
            registered_on=datetime.datetime.utcnow()
        )
        save_changes(new_user)
        response = {
            'status': 'OK',
            'message': 'User registered successfully',
        }
        return response, status.HTTP_201_CREATED
    else:
        response = {
            'status': 'FAIL',
            'message': 'User already exists. Please log in.'
        }
        return response, status.HTTP_409_CONFLICT


def get_all_users():
    return User.query.all()


def get_a_user(public_id):
    return User.query.filter_by(public_id=public_id).first()


def check_password(data):
    exists, user = user_exists(data)
    if not exists:
        response = {
            'status': 'FAIL',
            'message': 'User not found',
        }
        return response, status.HTTP_404_NOT_FOUND
    return user.check_password(data['password'])


def user_exists(data):
    if data.get('email', None) is not None:
        user = User.query.filter_by(email=data['email']).first()
        return user != None, user
    if data.get('username', None) is not None:
        user = User.query.filter_by(username=data['username']).first()
        return user != None, user
    return False, None


def generate_token(user):
    try:
        # generate the auth token
        auth_token = user.encode_auth_token(user.id)
        response = {
            'status': 'OK',
            'message': 'Successfully registered.',
            'authorization': auth_token.decode()
        }
        return response, status.HTTP_201_CREATED
    except Exception:
        response = {
            'status': 'FAIL',
            'message': 'Some error occurred, please try again.'
        }
        return response, status.HTTP_401_UNAUTHORIZED


def delete_user(user):
    db.session.delete(user)
    return db.session.commit()


def save_changes(data):
    db.session.add(data)
    db.session.commit()