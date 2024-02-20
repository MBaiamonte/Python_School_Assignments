from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import user


class Recipe:
    db='recipes_schema'
    def __init__(self,data):
        self.id=data['id']
        self.name=data['name']
        self.description=data['description']
        self.instructions=data['instructions']
        self.date_cooked=data['date_cooked']
        self.under_30=data['under_30']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
        self.creator= None

    @classmethod
    def save_new_recipe(cls, data):
        query="""INSERT INTO recipes (name, description, instructions, date_cooked,under_30,user_id) 
            VALUES (%(name)s,%(description)s,%(instructions)s,%(date_cooked)s,%(under_30)s,%(user_id)s);"""
        results= connectToMySQL(cls.db).query_db(query,data)
        return results

    @classmethod
    def get_one_recipe(cls, data):
        query="SELECT * FROM recipes WHERE id=%(id)s;"
        results=connectToMySQL(cls.db).query_db(query,data)
        return cls(results[0])

    @classmethod
    def get_one_recipe_with_user(cls, data):
        query='SELECT * FROM recipes JOIN users on recipes.user_id=users.id Where recipes.id=%(id)s;'
        results=connectToMySQL(cls.db).query_db(query,data)
        one_recipe=cls(results[0])
        user_data={
                'id':results[0]['users.id'],
                'first_name':results[0]['first_name'],
                'last_name':results[0]['last_name'],
                'email':results[0]['email'],
                'password':results[0]['password'],
                'updated_at':results[0]['users.updated_at'],
                'created_at':results[0]['users.updated_at']
            }
        one_recipe.creator=user.User(user_data)
        print("one recipes creator->", one_recipe.creator.first_name)
        return (one_recipe)


    @classmethod
    def get_all_recipes(cls):
        query='SELECT * FROM recipes'
        results=connectToMySQL(cls.db).query_db(query)
        all_recipes=[]
        for a_recipe in results:
            all_recipes.append(cls(a_recipe))
        return all_recipes

    @classmethod
    def get_all_recipes_with_users(cls):
        query="SELECT * FROM recipes JOIN users on recipes.user_id=users.id;"
        results=connectToMySQL(cls.db).query_db(query)
        all_recipes=[]
        for row in results:
            one_recipe=cls(row)
            user_data={
                'id':row['users.id'],
                'first_name':row['first_name'],
                'last_name':row['last_name'],
                'email':row['email'],
                'password':row['password'],
                'updated_at':row['users.updated_at'],
                'created_at':row['users.updated_at']
            }
            one_recipe.creator=user.User(user_data)
            all_recipes.append(one_recipe)
        return all_recipes
        
    @classmethod
    def delete_recipe(cls, data):
        query="DELETE FROM recipes WHERE id=%(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)

    @classmethod
    def update_recipe(cls, data):
        query= """UPDATE recipes
                set name=%(name)s,description=%(description)s,instructions=%(instructions)s,date_cooked=%(date_cooked)s,under_30=%(under_30)s
                WHERE id=%(id)s"""
        return connectToMySQL(cls.db).query_db(query,data)

    @staticmethod
    def validate_recipe_form(data):
        is_valid=True
        if len(data['name'])<3:
            is_valid=False
            flash("Name must be at least 3 characters long")
        if len(data['description'])<3:
            is_valid=False
            flash("Description must be at least 3 characters long")
        if len(data['instructions'])<3:
            is_valid=False
            flash("Instructions must be at least 3 characters long")
        if len(data['under_30'])==0:
            is_valid=False
            flash("under 30 was left blank")
        return is_valid
