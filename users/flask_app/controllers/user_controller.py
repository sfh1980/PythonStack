from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.user_model import User


@app.route('/')
def index():
    return redirect('/users')


@app.route('/users')
def users():
    return render_template("index.html",users=User.get_all())


@app.route('/user/new')
def new():
    return render_template("add_user.html")

@app.route('/user/create',methods=['POST'])
def create():
    print(request.form)
    User.save(request.form)
    return redirect('/users')


@app.route('/user/edit/<int:id>')
def edit(id):
    data ={
        "id":id
    }
    this_user = User.get_one(data)
    return render_template("edit_user.html", this_user=this_user)

@app.route('/user/show/<int:id>')
def show(id):
    data ={
        "id":id
    }
    one_user = User.get_one(data)
    return render_template("show_user.html", one_user=one_user)

@app.route('/user/update',methods=['POST'])
def update():
    User.update(request.form)
    return redirect('/users')

@app.route('/user/destroy/<int:id>')
def destroy(id):
    data ={
        'id': id
    }
    User.destroy(data)
    return redirect('/users')