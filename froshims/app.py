from flask import Flask, render_template, request

app = Flask(__name__)

SPORTS = ['Basketball', 'Soccer', 'Ultimate Frisbee']
REGISTRANTS = {}

@app.route('/')
def index():
    return render_template('index.html', sports = SPORTS)

@app.route('/register', methods = ['POST'])
def register():
    if not request.form.get('name'): 
        return render_template('failure.html', message = "Invalid name")
    elif request.form.get('sport') not in SPORTS:
        return render_template('failure.html', message = "Invalid sport(s)")
    for sport in request.form.getlist('sport'):
        if sport not in SPORTS:
            return render_template('failure.html')
    REGISTRANTS[request.form.get('name')] = request.form.getlist('sport')
    return render_template('success.html')