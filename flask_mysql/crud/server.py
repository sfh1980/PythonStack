from flask_app import app
from flask_app.controllers import dogs_controller, awards_controller



if __name__ == "__main__":
    app.run(debug=True)