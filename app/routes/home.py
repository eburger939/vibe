from flask import Blueprint, render_template
#Blueprint allows you to consolidate routes into a single bp object (similar to using router in js)
#render_template allows the route to respond with a template instead of a string 
bp = Blueprint('home', __name__, url_prefix='/')
from app.models import Vibe
from app.db import get_db

@bp.route('/')
def index():
    #get all Vibes
    db = get_db()
    vibes = db.query(Vibe).order_by(Vibe.created_at.desc()).all()
    return render_template(
        'homepage.html',
        vibes=vibes)

@bp.route('/login')
def login():
    return render_template('login.html')

@bp.route('/post/<id>')
def single(id):
    return render_template('single-post.html')