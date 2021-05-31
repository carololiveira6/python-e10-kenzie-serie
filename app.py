from flask import Flask, request, jsonify
from app.views.models import SeriesTable


app = Flask(__name__)

@app.route('/series', methods=['POST'])
def create():
    series = SeriesTable()
    data = request.get_json()

    return series.create_serie(data), 201

@app.route('/series', methods=['GET'])
def series():
    series = SeriesTable()

    return jsonify(series.return_data())

@app.route('/series/<int:serie_id>', methods=['GET'])
def select_by_id():
    series = SeriesTable()

    return jsonify(series.select_id())