from flask_app import app
from flask import render_template, redirect, request, flash, session
from flask_bcrypt import Bcrypt
from flask_app.models.users_model import User


bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('index.html')


#post method is validated using validate from model, if false, redirects to log in page
@app.route('/users/register', methods=["POST"])
def register():
    if not User.validate(request.form):
        return redirect('/')
    hashed_pass = bcrypt.generate_password_hash(request.form['password'])
    data = {
        **request.form,
        'password': hashed_pass
    }
    id = User.create(data)
    session['user_id'] = id
    return redirect('/welcome')

@app.route('/users/login', methods=["POST"])
def login():    
    #see if username/email provided exists in db
    data = {'email' : request.form['email']}
    user_in_db = User.get_by_email(data)
    #if user not registered
    if not user_in_db:
        flash('Invalid login info', 'log')
        return redirect('/')
    #if user exists, check password
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash('Invalid login info', 'log')
        return redirect('/')
    #log in
    session['user_id'] = user_in_db.id
    return redirect('/welcome')

@app.route('/users/logout')
def logout():
    del session['user_id']
    return redirect('/')


@app.route('/welcome')
def welcome():
    if 'user_id' not in session:
        return redirect('/')
    return render_template('welcome.html')