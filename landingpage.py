from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html",phrase="doesnt matter",times = 5)

def hello_world():
    return render_template('index.html')
#
@app.route('/ninjas')
def success():
    return render_template('ninjas.html')
#
@app.route('/dojos')
def dojos():
    return render_template('dojos.html')

@app.route('/users', methods=['POST'])
def create_user():
   name = request.form['name']
   email = request.form['email']
	 # Here's the line that changed. We're rendering a template from a post route now.
   return render_template('dojos.html')


app.run(debug=True)
