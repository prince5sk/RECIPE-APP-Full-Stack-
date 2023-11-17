from app.main import db


class SavedRecipe(db.Model):
    """ To save user's favorite recipe """
    __tablename__  = 'favorite_recipe'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    recipe_id = db.Column(db.Integer, unique=True, nullable=False)

    def __repr__(self):
        return f"<SavedRecipe recipe_id={self.recipe_id}>"