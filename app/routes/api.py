from flask import Blueprint, request, jsonify, session
from app.models import User, Vibe, Song, Vote 
from app.db import get_db
import sys

bp = Blueprint('api', __name__, url_prefix='/api')


@bp.route('/users', methods=['POST'])
def signup():
    data = request.get_json()
    db = get_db()
    try: 
        newUser = User(
            username= data['username'],
            email = data['email'],
            password = data['password']
        )
        db.add(newUser)
        db.commit()
    except:
        print(sys.exc_info()[0])
        #ensures thats db wont lock up when deployed to production environment (heroku)
        db.rollback()
        return jsonify(message = 'Signup failed'), 500

    session.clear()
    session['user_id'] = newUser.id
    session['loggedIn'] = True
    return jsonify(id = newUser.id)




@bp.route('/users/logout', methods=['POST'])
def logout():
    #remove session variables
    session.clear()
    return '', 204


@bp.route('/users/login', methods=['POST'])
def login():
    #check to see if users info already exists in the db, if not an error with throw and user needs to register
    data = request.get_json()
    db=get_db()

    try: 
        user = db.query(User).filter(User.email == data['email']).one()
        verifying = user.verify_password(data['password'])
        print('verifying', verifying)
    except:
        print(sys.exc_info()[0])
    
    if user.verify_password(data['password']) == False:
        return jsonify(message = 'Incorrect credentials'), 400

    session.clear()
    session['user_id'] = user.id
    session['loggedIn'] = True

    return jsonify(id=user.id)


@bp.route('/posts/upvote', methods=['PUT'])
def upvote():
    data = request.get_json()
    db = get_db()

    print('this is the data',data)

    try:
        #creating new vote with incoming id and session id
        newVote = Vote(
            song_id = data['song_id'],
            user_id = session.get('user_id')
        )
        db.add(newVote)
        db.commit()
    except:
        print(sys.exc_info()[0])

        db.rollback()
        return jsonify(message = "Upvote failed"), 500

    return '', 204