#controller is like traffic light telling which way to go
#helps to steer back-end and HTML
#its the middle man


from flask import render_template, request, redirect, session, flash
from flask_app import app
from flask_app.models.user_model import User

@app.route('/')
def index():
    return redirect('/users')


@app.route('/users')
def users():
    users = User.get_all()
    return render_template('users.html', all_users = users)

@app.route('/users/new')
def new_user():
    return render_template('new_user.html')

@app.route('/users/create', methods=['POST'])
def create_user():
    print(request.form)
    User.save(request.form)
    return redirect('/')