from flask_api import status

from app.main import db
from app.main.model.blacklist import BlacklistToken


def save_token(token):
    blacklist_token = BlacklistToken(token=token)
    try:
        # insert the token
        db.session.add(blacklist_token)
        db.session.commit()
        response = {
            'status': 'OK',
            'message': 'Successfully logged out'
        }
        return response, status.HTTP_200_OK
    except Exception as e:
        response = {
            'status': 'FAIL',
            'message': e
        }
        return response, status.HTTP_200_OK
