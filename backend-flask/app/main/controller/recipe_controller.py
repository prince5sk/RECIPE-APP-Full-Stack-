from flask import request, abort
from flask.json import jsonify
from flask_api import status as http_status
from flask_restx import Resource, Namespace, fields

from app import blueprint as bp
from ..util.dto import RecipeDto
from app.main.service import recipe_service as RecipeApi
from app.main.service.user_service import *


@bp.route('/recipe/<int:recipe_id>/summary', methods=['GET'])
def recipe_summary(recipe_id):
    return RecipeApi.get_recipe_summary(recipe_id)


@bp.route('/recipe/search', methods=['GET'])
def search_recipe():
    query = request.args.get('q', None)
    if query is None or len(query) == 0:
        abort(400)
    page = request.args.get('page', 1)
    return RecipeApi.search_recipes(q=query, page=page)




