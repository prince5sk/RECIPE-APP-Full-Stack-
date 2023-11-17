from app import app


@app.route('/')
def index(): 
    return "Recipe API 1.0"