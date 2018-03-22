
from app import db
from app.models import News, News_categories
from datetime import datetime, timedelta

news = News.query.all()
for u in news:
    db.session.delete(u)

cat_id1 = News_categories.query.filter_by(category='Geocronologia').first().id
cat_id2 = News_categories.query.filter_by(category='Hidrogeologia').first().id
cat_id3 = News_categories.query.filter_by(category='Economica').first().id

body = '''Breve introducao da noticia. Donec sed odio dui. Etiam porta 
        sem malesuada magna mollis euismod. Nullam id dolor id nibh ultricies vehicula ut id elit. 
        Morbi leo risus, porta ac consectetur ac, vestibulum at eros. Praesent commodo cursus magna.
        '''

intro = '''Breve introducao da noticia. Donec sed odio dui. Etiam porta 
        sem malesuada magna mollis euismod. Nullam id dolor id nibh ultricies vehicula ut id elit. 
        Morbi leo risus, porta ac consectetur ac, vestibulum at eros. Praesent commodo cursus magna.
        '''

now = datetime.utcnow()
n1 = News(title='Titulo da Noticia 1', category=cat_id1, body=body, intro=intro,
        date=now + timedelta(seconds=1))
n2 = News(title='Titulo da Noticia 2', category=cat_id2, body=body, intro=intro,
        date=now + timedelta(seconds=100))
n3 = News(title='Titulo da Noticia 3', category=cat_id3, body=body, intro=intro,
        date=now + timedelta(seconds=500))
n4 = News(title='Titulo da Noticia 4', category=cat_id2, body=body, intro=intro,
        date=now + timedelta(seconds=1000))

db.session.add_all([n1, n2, n3, n4])
db.session.commit()