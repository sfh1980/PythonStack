from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)

app.secret_key = "something_secret"

@app.route('/')
def root():
    print(session)

    if "count" not in session:
        session["count"] = 1
    else:
        session["count"] += 1

    return render_template('index.html')

@app.route('/add')
def add_one():
    return redirect('/')
    #click button

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')
    #reset button
















if __name__=="__main__":
    app.run(debug=True)