from functools import wraps

from flask import request
from flask_api import status as http_status

from app.main.service.auth_service import Auth


def token_requrired(f):
    @wraps(f)
    def decorated(*args, **kwargs):

        data, status = Auth.get_logged_in_user(request)
        token = data.get('data')

        if not token:
            return data, status
        
        return f(*args, **kwargs)
    
    return decorated


def admin_token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):

        data, status = Auth.get_logged_in_user(request)
        token = data.get('data')

        if not token: 
            return data, status
        
        admin = token.get('admin')
        if not admin:
            response = {
                'status': 'FAIL',
                'message': 'admin token required'
            }
            return response, http_status.HTTP_401_UNAUTHORIZED
        
        return f(*args, **kwargs)
    
    return decorated
