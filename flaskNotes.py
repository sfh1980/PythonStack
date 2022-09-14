
'''
virtual environments: used to control evrsions of our packages for our apps, walled off from the rest of our computer
    
    step 0: pip install pipenv - we run this ONCE to install it to our computer globally (does not matter where you run)
    
    step 0.1: python -m pipenv
    
    step 1: open cmder and navigate to the folder we will be working in
    
    step 2 :in cmder, run: pipenv install flask   
    this creates our virtual environment in the folder, and also installs flask
    
    step 3: in cmder, run: pipenv shell
    this makes our cmder enter the virtual environment
    
    step 4: in cmder, run: python server.py
    usually the file we're going to run is called server.py
    
    step 6: to exit server.py and return to the shell, we need to hit CTRL+C
    
    step 5: then we can run exit to leave the shell
    when were done working in the environment we run exit to leave

    ERROR:: --system is intended to be used for pre-existing Pipfile installation, not installation of specific packages. Aborting.

If you are using macOS, I deleted the project file in my virtualenv folder

Using GO I went to this folder -> ".local/share/virtualenvs/"
Take note of your project folder name, if your project folder is "myProject", in the virtualenv folder, you will see your project name with alphanumeric appended at its end, I simply moved to Bin
created a new project with "pipenv install" and the error was gone
Virtualenv location: /Users/your-computer-name/.local/share/virtualenvs/myProject-0dhhge


BOILER PLATE FOR server.py

from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.



from flask import Flask
app = Flask(__name__)
app.secret_key = "somebody_watching_me"



'''
# BOILER PLATE FOR installing pymysql

# # a cursor is the object we use to interact with the database
# import pymysql.cursors
# # this class will give us an instance of a connection to our database
# class MySQLConnection:
#     def __init__(self, db):
#         # change the user and password as needed
#         connection = pymysql.connect(host = 'localhost',
#                                     user = 'root', 
#                                     password = 'root', 
#                                     db = db,
#                                     charset = 'utf8mb4',
#                                     cursorclass = pymysql.cursors.DictCursor,
#                                     autocommit = True)
#         # establish the connection to the database
#         self.connection = connection
#     # the method to query the database
#     def query_db(self, query, data=None):
#         with self.connection.cursor() as cursor:
#             try:
#                 query = cursor.mogrify(query, data)
#                 print("Running Query:", query)
     
#                 cursor.execute(query, data)
#                 if query.lower().find("insert") >= 0:
#                     # INSERT queries will return the ID NUMBER of the row inserted
#                     self.connection.commit()
#                     return cursor.lastrowid
#                 elif query.lower().find("select") >= 0:
#                     # SELECT queries will return the data from the database as a LIST OF DICTIONARIES
#                     result = cursor.fetchall()
#                     return result
#                 else:
#                     # UPDATE and DELETE queries will return nothing
#                     self.connection.commit()
#             except Exception as e:
#                 # if the query fails the method will return FALSE
#                 print("Something went wrong", e)
#                 return False
#             finally:
#                 # close the connection
#                 self.connection.close() 
# # connectToMySQL receives the database we're using and uses it to create an instance of MySQLConnection
# def connectToMySQL(db):
#     return MySQLConnection(db)

# EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
#patter validation for email addresses
# import re for EMAIL_REGEX




#     >>>>>>>>>>>>>>>>>>>>>>>>