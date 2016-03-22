from flask import Flask, render_template
from flask.ext.script import Manager

app = Flask(__name__)

manager = Manager(app)

# Serves the initial website
@app.route('/')
def index():
    return render_template('index.html')

# Serves JSON for characters
@app.route('/characters')
def characters():
    return 0

# Serves JSON for comics
@app.route('/comics')
def comics():
    return 0

# Serves JSON for creators
@app.route('/creators')
def creators():
    return 0

if __name__ == '__main__':
    manager.run()
