import requests
from typing import List
from flask import request, abort
from flask_api import status as http_status

from app.settings import SPOONACULAR_API_KEY as api_key
from app.main import db

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
}

recipe_base_url = "https://api.spoonacular.com/recipes/"


def ensureApiKey(): 
    if not api_key:
        raise AssertionError('FATAL: Api key not found')

def search_recipes(q: str, page: int):
    ensureApiKey()
    print('\nD: search_recipies called with q={}, page={}'.format(q, page))
    
    url = recipe_base_url + 'complexSearch'
    if page == 1:
        offset = 0
    else:
        offset = int(page) * 10
    params = {
        'apiKey': api_key,
        'query': q,
        'number': 10,
        'offset': offset,
    }
    print('\nD: searching url={} params={}'.format(url, params))

    try:
        search_result = requests.get(url, params=params, timeout=5)
        print('\nD: search request = {}'.format(search_result.request.url))
        print('\nD: search result = {}'.format(search_result))
        result_json = search_result.json()
        return result_json
    except Exception as e:
        print(e)
    

def get_recipe_summary(recipe_id: int): 
    ensureApiKey()

    url = recipe_base_url + '{}/summary'.format(recipe_id)
    params = {
        'apiKey': api_key
    }
    return requests.get(url, params).json()


def getMultipleRecipes(ids: List[str]):
    ensureApiKey()

    url = recipe_base_url + 'informationBulk'
    params = {
        'apiKey': api_key,
        'ids': ids.join(','),
    }

    results = requests.get(url, params).json()
    return { 'results': results }

