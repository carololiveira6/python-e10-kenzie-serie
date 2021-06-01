from flask import Flask, request, jsonify, Blueprint
from ..services.models_services import SeriesTable

bp_series_views = Blueprint('series', __name__, url_prefix='/api')

@bp_series_views.route('/series', methods=['POST'])
def create():
    series = SeriesTable()
    data = request.get_json()

    return series.create_serie(data), 201

@bp_series_views.route('/series', methods=['GET'])
def series():
    series = SeriesTable()

    return jsonify({"data": series.return_data()})

@bp_series_views.route('/series/<int:serie_id>', methods=['GET'])
def select_by_id(serie_id):
    series = SeriesTable()

    return series.select_id(serie_id)