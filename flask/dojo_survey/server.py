from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)

app.secret_key = "do_you_know_the_muffin_man"

@app.route('/')
def render_survey():
    return render_template('/index.html')

@app.route('/submitted_page', methods=['POST'])
def submitted_page():
    session['name_field'] = request.form['name_field']
    session['location_dropdown'] = request.form['location_dropdown']
    session['fave_language'] = request.form['fave_language']
    session['commentbox'] = request.form['commentbox']
    
    return redirect('/show_results')


@app.route('/show_results')
def show_results():
    name_field = session['name_field']
    location_dropdown = session['location_dropdown']
    fave_language = session['fave_language']
    commentbox = session['commentbox']


    return render_template('submitted_page.html',
    name_field=name_field, 
    location_dropdown=location_dropdown, 
    fave_language=fave_language, 
    commentbox=commentbox)


if __name__=="__main__":
    app.run(debug=True)