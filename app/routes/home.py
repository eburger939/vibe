from flask import Blueprint, render_template
#Blueprint allows you to consolidate routes into a single bp object (similar to using router in js)
#render_template allows the route to respond with a template instead of a string 
bp = Blueprint('home', __name__, url_prefix='/')

@bp.route('/')
def index():
    return render_template('homepage.html')

@bp.route('/login')
def login():
    return render_template('login.html')

@bp.route('/post/<id>')
def single(id):
    return render_template('single-post.html')