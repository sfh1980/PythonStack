from operator import le
import queue
from winreg import QueryInfoKey
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
from flask_app.models import user_model


#call and constructor
class Recipe:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date_cooked = data['date_cooked']
        self.under_30 = data['under_30']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']



    @classmethod
    def create(cls,data):
        query = "INSERT INTO recipes (name, description, instructions, date_cooked, under_30, user_id) VALUES (%(name)s, %(description)s, %(instructions)s, %(date_cooked)s, %(under_30)s,  %(user_id)s)"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes JOIN users on recipes.user_id = users.id;"
        results = connectToMySQL(DATABASE).query_db(query)
        if results:
            all_recipes = []
            for row in results:
                this_recipe = cls(row)
                user_data = {
                    **row,
                    'id': row['users.id'],
                    'created_at': row['created_at'],
                    'updated_at': row['updated_at']
                }
                this_user = user_model.User(user_data)
                this_recipe.planner = this_user
                all_recipes.append(this_recipe)
            return all_recipes
        return []

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM recipes WHERE id = %(id)s"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM recipes JOIN users on users.id = recipes.user_id WHERE recipes.id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if len(results) < 1:
            return False
        row = results[0]
        this_recipe = cls(row)
        user_data = {
            **row,
            'id': row['users.id'],
            'created_at': row['created_at'],
            'updated_at': row['updated_at']
        }
        planner = user_model.User(user_data)
        this_recipe.planner = planner
        return this_recipe

    @classmethod
    def update(cls,data):
        query = "UPDATE recipes SET what = %(what)s, location = %(location)s, date = %(date)s, all_ages = %(all_ages)s, description = %(description)s WHERE id = %(id)s"
        return connectToMySQL(DATABASE).query_db(query, data)

    @staticmethod
    def validate(form_data):
        is_valid = True
        print(form_data,'======================================================')
        if len(form_data['name']) < 1:
            flash('name required')
            is_valid = False
        if len(form_data['description']) < 1:
            flash('description required')
            is_valid = False
        if len(form_data['instructions']) < 1:
            flash('instructions required')
            is_valid = False
        if len(form_data['date_cooked']) < 1:
            flash('date_cooked required')
            is_valid = False
        if 'under_30' not in form_data:
            flash('Under 30: required')
            is_valid = False
        return is_valid
