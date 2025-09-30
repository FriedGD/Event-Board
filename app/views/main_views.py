from flask import Blueprint, render_template, url_for, request
from app.database import init_db, Event, add_event, get_event, get_event_forum, edit_event, archive_event, restore_event, delete_event
from werkzeug.utils import redirect

bp = Blueprint('main', __name__, url_prefix="/")

init_db()

@bp.route("/")
def index():
    return redirect(url_for('main.forum'))

@bp.route("/forum")
def forum():
    event_list = get_event_forum(False)
    return render_template('events.html', event_list=event_list)

@bp.route("/archive")
def archive():
    event_list = get_event_forum(True)
    return render_template('archive.html', event_list=event_list)

@bp.route("/add", methods=('POST',))
def add():
    subject = request.form['subject']
    author = request.form['author']
    content = request.form['content']
    add_event(subject, author, content)
    return redirect(url_for('main.forum'))

@bp.route("/edit/<int:event_id>", methods=('POST',))
def edit(event_id):
    content = request.form['edited']
    edit_event(event_id, content)
    return redirect(url_for('main.forum'))

@bp.route("/archiving/<int:event_id>", methods=('POST','GET'))
def archiving(event_id):
    archive_event(event_id)
    return redirect(url_for('main.forum'))

@bp.route("/restore/<int:event_id>", methods=('POST','GET'))
def restore(event_id):
    restore_event(event_id)
    return redirect(url_for('main.archive'))

@bp.route("/delete/<int:event_id>", methods=('POST','GET'))
def delete(event_id):
    delete_event(event_id)
    return redirect(url_for('main.archive'))
