
from app import db
from app.models import News, News_categories, Publications, Publication_categories, Authors, Team
from datetime import datetime, timedelta


def News_db():
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
        title= 'Titulo da Noticia'
        now = datetime.utcnow()
        n1 = News(title=title, category=cat_id1, body=body, intro=intro,
                date=now + timedelta(seconds=1))
        n2 = News(title=title, category=cat_id2, body=body, intro=intro,
                date=now + timedelta(seconds=100))
        n3 = News(title=title, category=cat_id3, body=body, intro=intro,
                date=now + timedelta(seconds=500))
        n4 = News(title=title, category=cat_id2, body=body, intro=intro,
                date=now + timedelta(seconds=1000))
        n5 = News(title=title, category=cat_id1, body=body, intro=intro,
                date=now + timedelta(seconds=1200))
        n6 = News(title=title, category=cat_id2, body=body, intro=intro,
                date=now + timedelta(seconds=1500))
        n7 = News(title=title, category=cat_id3, body=body, intro=intro,
                date=now + timedelta(seconds=2000))
        n8 = News(title=title, category=cat_id2, body=body, intro=intro,
                date=now + timedelta(seconds=2200))
        n9 = News(title=title, category=cat_id1, body=body, intro=intro,
                date=now + timedelta(seconds=2500))
        n10 = News(title=title, category=cat_id2, body=body, intro=intro,
                date=now + timedelta(seconds=3000))
        n11 = News(title=title, category=cat_id3, body=body, intro=intro,
                date=now + timedelta(seconds=3200))
        n12 = News(title=title, category=cat_id2, body=body, intro=intro,
                date=now + timedelta(seconds=3500))

        db.session.add_all([n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11, n12])
        db.session.commit()

def Pub_db():
        pubs = Publications.query.all()
        for u in pubs:
                db.session.delete(u)
        pubs_c = Publication_categories.query.all()
        for u in pubs_c:
                db.session.delete(u)
        auth = Authors.query.all()
        for u in auth:
                db.session.delete(u)
        db.session.commit()

        c1 = Publication_categories(category='Economica')
        c2 = Publication_categories(category='Modelamento')
        c3 = Publication_categories(category='Tectonica') 

        db.session.add_all([c1, c2, c3])
        db.session.commit()

        cat_id1 = Publication_categories.cat_id(category='Economica')
        cat_id2 = Publication_categories.cat_id(category='Modelamento')
        cat_id3 = Publication_categories.cat_id(category='Tectonica')

        auth1 = Authors(name='Andrew Peter James', abrev='James A.J.')
        auth2 = Authors(name='Bob Dilan', abrev='Dilan B.')
        auth3 = Authors(name='Oliver Twist', abrev='Oliver T.')
        auth4 = Authors(name='James Goodman', abrev='Goodman J.')

        db.session.add_all([auth1, auth2, auth3, auth4])
        db.session.commit()

        intro = '''Some quick example text to build on the card title and make up the bulk of the card's content. 
        Some quick example text to build on the card title and make up the bulk of the card's content...'''

        now = datetime.utcnow()
        p1 = Publications(title='Titulo Publicação1 Titulo Publicação Titulo Publicação Titulo Publicação Titulo Publicação', category=cat_id1, file_dir='/static/imgs/aaaa.jpg', abstract=intro,
                date=now + timedelta(seconds=1), img_dir="/static/imgs/Pub_1_.jpg")
        p2 = Publications(title='Titulo Publicação2 Titulo Publicação Titulo Publicação Titulo Publicação Titulo Publicação', category=cat_id2, file_dir='/static/imgs/aaaa.jpg', abstract=intro,
                date=now + timedelta(seconds=1000), img_dir="/static/imgs/Pub_2.png")
        
        p3 = Publications(title='Titulo Publicação3 Titulo Publicação Titulo Publicação Titulo Publicação Titulo Publicação', category=cat_id3, file_dir='/static/imgs/aaaa.jpg', abstract=intro,
                date=now + timedelta(seconds=10000), img_dir="/static/imgs/Pub_3.jpg")

        p1.authors.append(auth1)
        p1.authors.append(auth2)
        p1.authors.append(auth3)
        p1.authors.append(auth4)
        p2.authors.append(auth2)
        p2.authors.append(auth3)
        p2.authors.append(auth4)
        p3.authors.append(auth1)
        p3.authors.append(auth4)

        db.session.add_all([p1, p2, p3])
        db.session.commit()

     
def Team_db():
        team = Team.query.all()
        for u in team:
                db.session.delete(u)

        intro = '''
                Dmosnin ed osan pojd kaxsax ckdds a dolkcm sd cnoia. Dmosnin ed osan pojd kaxsax ckdds a dolkcm sd cnoia.
                Dmosnin ed osan pojd kaxsax ckdds a dolkcm sd cnoia. 
                '''

        now = datetime.utcnow()
        name1="Martin L. King"
        name2="Bob Dylan"
        name3="James Brown"
        name4="Dee Purple"
        name5="John Lenon"
        name6="Steve Jobs"

        role1="Diretor"
        role2="Pesquisador"
        role3="Pesquisador Chefe"

        t1 = Team(name=name1, role=role1, intro=intro, foto="/static/imgs/face.jpg")
        t2 = Team(name=name2, role=role3, intro=intro, foto="/static/imgs/face.jpg")
        t3 = Team(name=name3, role=role2, intro=intro, foto="/static/imgs/face.jpg")
        t4 = Team(name=name4, role=role2, intro=intro, foto="/static/imgs/face.jpg")
        t5 = Team(name=name5, role=role2, intro=intro, foto="/static/imgs/face.jpg")
        t6 = Team(name=name6, role=role2, intro=intro, foto="/static/imgs/face.jpg")


        db.session.add_all([t1, t2, t3, t4, t5, t6])
        db.session.commit()
News_db()