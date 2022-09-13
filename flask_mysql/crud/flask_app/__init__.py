from flask import Flask
app = Flask(__name__)
app.secret_key = "somebody_watching_me"
DATABASE = 'dogs_db'