from flask import Flask, jsonify, json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def getHi():
    return "ola mundo"

@app.route('/menu')
def getMenu():
    with open('menu.json','r') as json_file:
        menu = json.load(json_file)
    return menu

@app.route('/reviews')
def getReviews():
    with open('reviews.json','r') as json_file:
        reviews = json.load(json_file)
    return reviews

app.run(port=5000, host='localhost')