from flask import Flask , request , jsonify , make_response

app = Flask(__name__)

@app.route("/")
def index():
    return "<p>Hello, World!</p>"