from flask import Flask, render_template
from flask.ext.script import Manager

app = Flask(__name__)

manager = Manager(app)

# Serves JSON for characters
@app.route('/api/characters')
def characters():
    return 0

# Serves JSON for comics
@app.route('/api/comics')
def comics():
    return 0

# Serves JSON for creators
@app.route('/api/creators')
def creators():
    return 0

# Serves the initial website (the catch-all is to facilitate react-router routes)
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return render_template('index.html')


if __name__ == '__main__':
    manager.run()
