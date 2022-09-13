from flask_app.config.mysqlconnection import connectToMySQL
from side_stuff.users_crud.flask_app.config.mysqlconnection import MySQLConnection

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def save(cls,data):
        query = 'INSERT INTO users(first_name, last_name, email) VALUES(%(first_name)s, %(last_name)s, %(email)s);'
        result = connectToMySQL('users_schema').query_db(query,data)

        return result


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        result = connectToMySQL(mysql_db).query_db(query)
        print("------------------------------------")
        print("This is the results of the get all query")
        print("---------------------------------------")

        users = []

