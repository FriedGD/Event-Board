from flask import Flask
from app.database import Event, init_db, add_event, get_event, edit_event, archive_event, delete_event

def create_app():
    app = Flask(__name__)

    init_db()

    from .views import main_views
    app.register_blueprint(main_views.bp)

    return app