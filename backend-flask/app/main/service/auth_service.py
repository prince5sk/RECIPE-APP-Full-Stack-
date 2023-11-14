from flask_api import status

from app.main.model.user import User
from app.main.service.blacklist_service import save_token


class Auth: 

    @staticmethod
    def login_user(data):
        try:
            user = User.query.filter_by(email=data.get('email')).first()
            if user and user.check_password(data.get('password')):
                auth_token = user.encode_auth_token(user.id)
                return {
                    'status': 'OK',
                    'message': 'Login Successful',
                    'data': {
                        'user_id': user.id,
                        'email': user.email,
                        'public_id': user.public_id,
                        'username': user.username,
                        'admin': user.admin,
                        'registered_on': str(user.registered_on)
                    },
                    'authorization': auth_token
                }, status.HTTP_200_OK
            else:  
                return {
                    'status': 'FAIL',
                    'message': 'Email or Password does not match'
                }, status.HTTP_401_UNAUTHORIZED
        except Exception as e:
            print(e)
            return {
                'status': 'FAIL',
                'message': 'Try again',
            }, status.HTTP_500_INTERNAL_SERVER_ERROR
    
    @staticmethod
    def logout_user(data):
        if data:
            auth_token = data.split(' ')[1]
        else:
            auth_token = ''
        if auth_token:
            resp = User.decode_auth_token(auth_token)
            if not isinstance(resp, str):
                # mark the token as blacklisted
                return save_token(auth_token)
            else:
                response = {
                    'status': 'FAIL',
                    'message': resp
                }
                return response, status.HTTP_401_UNAUTHORIZED
        else:
            response = {
                'status': 'FAIL',
                'message': 'Provide a valid auth token.'
            }
            return response, status.HTTP_403_FORBIDDEN
        
    @staticmethod
    def get_logged_in_user(new_request):
        # get the auth token
        auth_token = new_request.headers.get('Authorization')
        if auth_token:
            resp = User.decode_auth_token(auth_token)
            if not isinstance(resp, str):
                user = User.query.filter_by(id=resp).first()
                response = {
                    'status': 'OK',
                    'data': {
                        'user_id': user.id,
                        'email': user.email,
                        'admin': user.admin,
                        'registered_on': str(user.registered_on)
                    }
                }
                return response, status.HTTP_200_OK
            response = {
                'status': 'FAIL',
                'message': resp
            }
            return response, status.HTTP_401_UNAUTHORIZED
        else:
            response = {
                'status': 'FAIL',
                'message': "Provide a valid auth token."
            }
            return response, status.HTTP_401_UNAUTHORIZED
