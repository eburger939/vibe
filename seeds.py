from app.models import User, Song
from app.db import Session, Base, engine


#drop and rebuild tables
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

#session required for any time a crud operation is performed on the mysql table
db = Session()
# insert users
db.add_all([
  User(username='alesmonde0', email='nwestnedge0@cbc.ca', password='password123'),
  User(username='jwilloughway1', email='rmebes1@sogou.com', password='password123'),
  User(username='iboddam2', email='cstoneman2@last.fm', password='password123'),
  User(username='dstanmer3', email='ihellier3@goo.ne.jp', password='password123'),
  User(username='djiri4', email='gmidgley4@weather.com', password='password123')
])

#actually inserts into the database
db.commit()

######################
#seed song information
######################
# insert posts
db.add_all([
  Song(title='Dont stop believing', author='Journey', song_url='', user_id=1),
  Song(title='Billie Jean', author='Michael Jackson', song_url='', user_id=1),
  Song(title='Take on me', author='A-ha', song_url='', user_id=2),
  Song(title='Beat it', author="Michael Jackson", song_url='', user_id=3),
  Song(title='Tainted love', author='Soft Cell', song_url='', user_id=4)
])

db.commit()



db.close()