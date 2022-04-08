from flask import Flask, render_template
app = Flask(__name__)    
@app.route('/')          
def hello_world():
    return render_template('index.html', x = 8, y = 8) 

@app.route('/<y2>')          
def dojo(y2):
    return render_template('index.html', x = 8, y = int(y2)) 

@app.route('/<y3>/<x3>')          
def say(y3, x3):
    return render_template('index.html', x = int(x3), y = int(y3))


if __name__=="__main__":  
    app.run(debug=True)    
