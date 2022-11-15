from app.models import User, Song, Vote, Vibe
from app.db import Session, Base, engine


#drop and rebuild tables
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

#session required for any time a crud operation is performed on the mysql table
db = Session()
# insert users
db.add_all([
  User(username='Braiton', email='nwestnedge0@cbc.ca', password='password123'),
  User(username='Stacy', email='rmebes1@sogou.com', password='password123'),
  User(username='Emily', email='cstoneman2@last.fm', password='password123'),
  User(username='Otter', email='ihellier3@goo.ne.jp', password='password123'),
  User(username='djiri4', email='gmidgley4@weather.com', password='password123')
])

#actually inserts into the database
db.commit()

######################
#seed vibes
######################
db.add_all([
  Vibe(vibe_name='Braitons house party', user_id=1),
  Vibe(vibe_name='Stacys workout class', user_id=2),
  Vibe(vibe_name='Emilys christmas party', user_id=3),
  Vibe(vibe_name='Otters sleepy time', user_id=4)
])

######################
#seed song information
######################
db.add_all([
  Song(title='Dont stop believing', author='Journey', song_url='', user_id=1, vibe_id=1), 
  Song(title='Billie Jean', author='Michael Jackson', song_url='', user_id=1, vibe_id=1),
  Song(title='Take on me', author='A-ha', song_url='', user_id=2, vibe_id=2),
  Song(title='Beat it', author="Michael Jackson", song_url='', user_id=3, vibe_id=3),
  Song(title='Tainted love', author='Soft Cell', song_url='', user_id=4, vibe_id=4)
])

db.commit()

######################
#seed votes
######################
db.add_all([
  Vote(user_id=1, song_id=2),
  Vote(user_id=1, song_id=4),
  Vote(user_id=2, song_id=4),
  Vote(user_id=3, song_id=4),
  Vote(user_id=4, song_id=2)
])

db.commit()

db.close()