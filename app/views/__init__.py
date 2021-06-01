from .series_views import bp_series_views

def init_app(app):
    app.register_blueprint(bp_series_views)