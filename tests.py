from datetime import datetime, timedelta
import unittest
from app import app, db
from app.models import News, News_categories, Publications, Publication_categories, Authors, Publication_authors

class UserModelCase(unittest.TestCase):
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_news_index(self):
        c1 = News_categories(category='c1')
        c2 = News_categories(category='c2')
        c3 = News_categories(category='c3') 

        db.session.add_all([c1, c2, c3])
        db.session.commit()

        cat_id1 = News_categories.cat_id(category='c2')
        cat_id2 = News_categories.cat_id(category='c1')

        body1 = 'AAAAAAAAAAAAAAAABBBBBBBBBBBBBBBBB CCCCCCCCCCCC CCCCCCCCCCCCCC SSSSSSSSSSS'
        body2 = 'CCCCCCCCCCCC CCCCCCCCCCCCCC SSSSSSSSSSS'
        body3 = 'AAAAAAAAAAAAAAAABBBBBBBBBBBBBBBBB'

        intro = 'introoo'

        now = datetime.utcnow()
        n1 = News(title='N1', category=cat_id1, body=body1, intro=intro,
                date=now + timedelta(seconds=1))
        n2 = News(title='N2', category=cat_id2, body=body2, intro=intro,
                date=now + timedelta(seconds=100))
        n3 = News(title='N3', category=cat_id1, body=body3, intro=intro,
                date=now + timedelta(seconds=500))
        n4 = News(title='N4', category=cat_id2, body=body1, intro=intro,
                date=now + timedelta(seconds=1000))

        db.session.add_all([n1, n2, n3, n4])
        db.session.commit()
        
        print (News.index_news())
        self.assertEqual(News.index_news().count(), 3)

    def test_pubs_index(self):
        c1 = Publication_categories(category='c1')
        c2 = Publication_categories(category='c2')
        c3 = Publication_categories(category='c3') 

        db.session.add_all([c1, c2, c3])
        db.session.commit()

        cat_id1 = Publication_categories.cat_id(category='c2')
        cat_id2 = Publication_categories.cat_id(category='c1')

        auth1 = Authors(name='Andrew Peter James', abrev='James A.J.')
        auth2 = Authors(name='Bob Dilan', abrev='Dilan B.')

        db.session.add_all([auth1, auth2])
        db.session.commit()

        body1 = 'AAAAAAAAAAAAAAAABBBBBBBBBBBBBBBBB CCCCCCCCCCCC CCCCCCCCCCCCCC SSSSSSSSSSS'
        body2 = 'CCCCCCCCCCCC CCCCCCCCCCCCCC SSSSSSSSSSS'
        body3 = 'AAAAAAAAAAAAAAAABBBBBBBBBBBBBBBBB'

        intro = 'introoo'

        now = datetime.utcnow()
        p1 = Publications(title='P1', category=cat_id1, file_dir='/static/imgs/aaaa.jpg', abstract=intro,
                date=now + timedelta(seconds=1))
        p2 = Publications(title='P2', category=cat_id2, file_dir='/static/imgs/aaaa.jpg', abstract=intro,
                date=now + timedelta(seconds=1000))
        
        p3 = Publications(title='P3', category=cat_id1, file_dir='/static/imgs/aaaa.jpg', abstract=intro,
                date=now + timedelta(seconds=10000))

        p1a1 = Publication_authors(pub_id=p1.id, auth_id=auth1.id)
        p1a2 = Publication_authors(pub_id=p1.id, auth_id=auth2.id)
        p2a = Publication_authors(pub_id=p2.id, auth_id=auth2.id)
        p3a = Publication_authors(pub_id=p3.id, auth_id=auth1.id)

        db.session.add_all([p1, p2, p3])
        db.session.add_all([p1a1, p1a2, p2a, p3a])
        db.session.commit()

        self.assertEqual(Publications.index_pubs().count(), 3)

if __name__ == '__main__':
    unittest.main(verbosity=2)

