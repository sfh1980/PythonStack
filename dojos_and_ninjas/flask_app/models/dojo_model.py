from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask_app.models.ninja_model import Ninja



class Dojo:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []


    @classmethod
    def create(cls,data):
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"
        return connectToMySQL(DATABASE).query_db(query,data)
        

    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM dojos WHERE ID = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if len(results) > 0:
            dojo_instance = cls(results[0])
            return dojo_instance
        return False

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(DATABASE).query_db(query)        
        all_dojos = []
        print(results)
        for row_from_db in results:
            dojo_instance = cls(row_from_db)            
            all_dojos.append(dojo_instance)
        return all_dojos


    @classmethod
    def get_one_with_ninjas(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas on dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query,data)
        print(results)
        dojo = cls(results[0])
        for row_from_db in results:
            n = {
                'id': row_from_db['ninjas.id'],
                'first_name': row_from_db['first_name'],
                'last_name': row_from_db['last_name'],
                'age': row_from_db['age'],
                'created_at': row_from_db['created_at'],
                'updated_at': row_from_db['updated_at']
            }
            dojo.ninjas.append(Ninja(n))
        return dojo