from flask import Flask, request, jsonify
from app.views.models import SeriesTable

env = Env()
env.read_venv()

app = Flask(__name__)

@app.route('/series', methods=['POST'])
def create():

    series = SeriesTable()
    data = request.get_json()

    return series.create_serie(data), 201

@app.route('/series', methods=['GET'])
def series():
    pass
