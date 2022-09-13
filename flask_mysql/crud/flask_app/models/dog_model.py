from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask_app.models import award_model
from flask import flash





class Dog:#below matches up to attributes set up in ERD
    def __init__(self,data): #set to make off of dictionaries
        self.id = data['id'] #alt+shift+down copy/paste line below
        self.name = data['name'] #ctrl+d highlights same values
        self.breed = data['breed'] 
        self.color = data['color'] 
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
#give init a dictionary with all keys of Dog, will instantiate a Dog


    #all queries will be classmethods
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dogs;"
        results = connectToMySQL(DATABASE).query_db(query)
        #creates connection to mysqlconnection>class
        # print(results)
        all_dogs = []
        for row_from_db in results:
            dog_instance = cls(row_from_db)
            #call the class cls. instantiate will call the above init
            #will return a dog instance based off dictionary of lists
            all_dogs.append(dog_instance)
        return all_dogs

#above makes query to database to get all dogs, then loop over results
#which is a list of dictionaries

    @classmethod
    def create(cls, data):
        query ="INSERT INTO dogs (name, breed, color, age) VALUES (%(name)s, %(breed)s, %(color)s, %(age)s);"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod #query to get one dog
    def get_one(cls, data):
        query = "SELECT * FROM dogs WHERE id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query,data)
        if len(results) > 0:
            dog_instance = cls(results[0])
            return dog_instance
        return False

    @classmethod
    def get_one_with_awards(cls,data):
        query = "SELECT * FROM dogs LEFT JOIN awards ON dogs.id = awards.dog_id WHERE dogs.id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query,data)
        print(results)
        if len(results) > 0:
            dog_instance = cls(results[0])
            award_list = []
            for row_from_db in results:
                award_data = {
                    'id': row_from_db['awards.id'],
                    'title': row_from_db['title'],
                    'created_at': row_from_db['awards.created_at'],
                    'updated_at': row_from_db['awards.updated_at'],
                    'dog_id': row_from_db['dog_id']
                }
                award_instance = award_model.Award(award_data)
                award_list.append(award_instance)
            dog_instance.award_list = award_list        
            return dog_instance
        return False


    @classmethod
    def update(cls,data):
        query = "UPDATE dogs SET name = %(name)s, breed = %(breed)s, color = %(color)s, age = %(age)s WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)

    @classmethod
    def delete(cls,data):
        query = "DELETE FROM dogs WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)

    @classmethod
    def validator(data):
        is valid = True

        if len(data[name]) <= 0:
            print("name is not valid")
            is_valid = False

        if len(data[breed]) <= 0:
            print("breed is not valid")
            is_valid = False

        if len(data[color]) <= 0:
            print("color is not valid")
            is_valid = False

        if len(data[age]) <= 0:
            print("age is not valid")
            is_valid = False


        return is_valid