from flask import flask

app = Flask(__name__)

if __name__ == '__main__':
    # Fire up Flask test server
    app.run(debug=True, use_reloader=True)