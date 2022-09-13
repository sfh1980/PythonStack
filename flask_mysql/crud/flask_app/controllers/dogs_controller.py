from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.dog_model import Dog

#get all
@app.route('/')
def index():
    all_dogs = Dog.get_all()
    return render_template('index.html', all_dogs=all_dogs)

#get one
@app.route('/dogs/<int:id>')
def one_dog(id):
    one_dog = Dog.get_one_with_awards({'id':id})
    return render_template('one_dog.html', one_dog=one_dog)

#new dog form
@app.route('/dogs/new')
def new_dog_form():
    return render_template('dogs_new.html')

#processes new dog form
@app.route('/dogs/create', methods=['POST'])
def create_dog():
    name = request.form['name']
    if len(name) <= 0:
        print("name is not valid")
        return redirect('/dogs/new')
    breed = request.form['breed']
    if len(breed) <= 0:
        print("breed is not valid")
        return redirect('/dogs/new')
    color = request.form['color']
    if len(color) <= 0:
        print("color is not valid")
        return redirect('/dogs/new')
    age = request.form['age']
    if len(age) <= 0:
        print("age is not valid")
        return redirect('/dogs/new')
    Dog.create(request.form)
    return redirect('/')


#edit dog form
@app.route('/dogs/<int:id>/edit')
def edit_dog_form(id):
    data = {
        'id':id
    }
    this_dog = Dog.get_one(data)
    return render_template('dogs_edit.html', this_dog=this_dog)


#process edit dog form
@app.route('/dogs/<int:id>/update', methods=['POST'])
def update_dog(id):
    data = {
        **request.form,
        'id':id
    }
    Dog.update(data)
    return redirect('/')


#delete dog by id
@app.route('/dogs/<int:id>/delete')
def delete_dog(id):
    data = {
        'id':id
    }
    Dog.delete(data)
    return redirect('/')