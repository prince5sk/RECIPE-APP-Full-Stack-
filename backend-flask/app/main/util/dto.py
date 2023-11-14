from flask_restx import Namespace, fields
from app.main.service.user_service import get_a_user


class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        # 'password': fields.String(required=True, description='user password'),
        'username': fields.String(description='user username'),
        'public_id': fields.String(description='user Identifier'),
        'admin': fields.Boolean(description='is admin'),
        'registered_on': fields.DateTime(description="registered date"),
    })


class AuthDto:
    api = Namespace('auth', description='authentication realted options')
    user_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='user email'),
        'password': fields.String(required=True, description='usere password')
    })


"""
"results": [
        {
            "id": 716429,
            "title": "Pasta with Garlic, Scallions, Cauliflower & Breadcrumbs",
            "image": "https://spoonacular.com/recipeImages/716429-312x231.jpg",
            "imageType": "jpg",
        },
        {
            "id": 715538,
            "title": "What to make for dinner tonight?? Bruschetta Style Pork & Pasta",
            "image": "https://spoonacular.com/recipeImages/715538-312x231.jpg",
            "imageType": "jpg",
        }
    ],
"""
class RecipeDto:
    api = Namespace('recipe', description='recipe related operations')