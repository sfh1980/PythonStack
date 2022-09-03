
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
'''