from timeit import repeat
from turtle import color
from flask import Flask, render_template  
app = Flask(__name__)    







@app.route('/play')
def boxes():
    return render_template('index.html') 

@app.route('/play/<boxes>')
def more_boxes(boxes):
    return render_template('playground1.html', boxes = int(boxes))


@app.route('/play/<boxes>/<color>')
def color_change(boxes,color):
    return render_template('playground2.html', boxes = int(boxes), color = color)

















if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    