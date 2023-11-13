from flask_api import status

from app.main.model.user import User


class Auth: 

    @staticmethod
    def login_user(data):
        try:
            user = User.query.filter_by(email=data.get('email')).first()
            if user and user.check_password(data.get('password')):
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
                    }
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
