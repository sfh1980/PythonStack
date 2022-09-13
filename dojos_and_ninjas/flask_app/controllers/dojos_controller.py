from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.dojo_model import Dojo


@app.route('/')
def index():
    return redirect('/dojos')

@app.route('/dojos')
def dojos():
    dojos = Dojo.get_all()
    return render_template("index.html", all_dojos = dojos)

@app.route('/create_dojo', methods=['POST'])
def create_dojo():
    Dojo.create(request.form)
    return redirect('/dojos')


@app.route('/dojo/<int:id>')
def ndj_dojo(id):
    data = {
        "id": id
    }
    return render_template('create_dojo.html', dojo=Dojo.get_one_with_ninjas(data))








# @app.route('/')
# def index():
#     all_dojos = Dojo.get_all()
#     print(all_dojos)
#     return render_template('index.html', all_dojos=all_dojos)


# @app.route('/create_dojo', methods=["POST"])
# def create_dojo():
#     name = request.form['name']
#     Dojo.create(request.form)
#     return redirect('/')

# @app.route('/dojo/<int:id>/update')
# def update_dojo():
#     data = {
#         **request.form,
#         'id':id
#     }
#     Dojo.update(data)
#     return render_template('/')









