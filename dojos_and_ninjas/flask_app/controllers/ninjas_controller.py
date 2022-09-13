from flask import render_template, redirect, request
from flask_app import app
from flask_app.models import dojo_model, ninja_model


# @app.route('/new/ninja')
# def redirect_new_ninja():
#     return render_template('new_ninja.html')

@app.route('/ninjas')
def ninjas():
    return render_template('new_ninja.html', dojos= dojo_model.Dojo.get_all())



@app.route('/create/ninja', methods=["POST"])
def create_ninja():
    ninja_model.Ninja.create(request.form)
    return redirect('/')

