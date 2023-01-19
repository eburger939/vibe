from flask import Blueprint, render_template, session, redirect
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
        vibes=vibes,
        loggedIn=session.get('loggedIn'))



@bp.route('/login')
def login():
    #if user is already logged in then the dashboard will render and option to login will be removed 
    if session.get('loggedIn') is None:
        return render_template('login.html')
    return redirect('/dashboard')



@bp.route('/vibe/<id>')
def single(id):
    db = get_db()
    vibe = db.query(Vibe).filter(Vibe.id == id).one()
    return render_template(
        'single-vibe.html',
        vibe=vibe,
        loggedIn=session.get('loggedIn')
        )