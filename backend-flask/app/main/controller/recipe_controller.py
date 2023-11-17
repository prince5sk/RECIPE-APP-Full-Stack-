from flask import request, abort, Response
from flask.json import jsonify
from flask_api import status as http_status
from flask_restx import Resource, Namespace, fields

from app import blueprint as bp
from ..util.dto import RecipeDto
from app.main import db
from app.main.model.favorite_recipe import SavedRecipe
from app.main.service import recipe_service as RecipeApi
from app.main.service.user_service import *
from app.main.util.decorator import token_required


@bp.route('/recipes/<int:recipe_id>/summary', methods=['GET'])
def recipe_summary(recipe_id):
    return RecipeApi.get_recipe_summary(recipe_id)


@bp.route('/recipes/search', methods=['GET'])
def search_recipe():
    query = request.args.get('searchTerm', None)
    request.method
    if query is None or len(query) == 0:
        abort(http_status.HTTP_400_BAD_REQUEST)
    page = request.args.get('page', 1)
    return RecipeApi.search_recipes(q=query, page=page)


@bp.route('/recipes/favourite', methods=['POST', 'GET', 'DELETE'])
def favorite_recipe():
    recipe_id = request.form.get('recipeId')
    if recipe_id is None and request.get_json():
        recipe_id = request.get_json().get('recipeId')
    if recipe_id is None and request.method != 'GET':
        abort(http_status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'GET':
        recipes = SavedRecipe.query.all()
        print(type(recipes))
        recipe_ids = list(map(lambda r:str(r.recipe_id), recipes))
        print(recipe_ids)   
        favorites = RecipeApi.getMultipleRecipes(recipe_ids)
        return favorites, http_status.HTTP_200_OK
    elif request.method == 'DELETE':
        try:
            recipe = SavedRecipe.query.filter_by(recipe_id=recipe_id).first()
            db.session.delete(recipe)
            db.session.commit()
        except Exception as e:
            print(e)
            return "Try again", http_status.HTTP_500_INTERNAL_SERVER_ERROR
        return "Success", http_status.HTTP_204_NO_CONTENT
    elif request.method == 'POST':
        try:
            favorite = SavedRecipe.query.filter_by(recipe_id=recipe_id).first()
            if not favorite:
                new_favorite = SavedRecipe(recipe_id=recipe_id)
                db.session.add(new_favorite)
                db.session.commit()
            else:
                return "Already exists", http_status.HTTP_409_CONFLICT
        except Exception as e:
            print(e)
            return "Try again", http_status.HTTP_500_INTERNAL_SERVER_ERROR
        return "OK", http_status.HTTP_201_CREATED
    else:
        abort(http_status.HTTP_500_INTERNAL_SERVER_ERROR)


        




