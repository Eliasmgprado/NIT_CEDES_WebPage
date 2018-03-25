# -*- coding: utf-8 -*-

from app import db
from app.models import (News, News_categories, News_imgs,
                         Publications, Publication_categories, Publication_imgs, Publication_type, 
                         Authors, Team)
from datetime import datetime, timedelta


def News_db():
        news = News.query.all()
        for u in news:
                db.session.delete(u)
        news_c = News_categories.query.all()
        for u in news_c:
                db.session.delete(u)
        db.session.commit()

        c1 = News_categories(category='Geocronologia')
        c2 = News_categories(category='Hidrogeologia')
        c3 = News_categories(category='Economica') 

        db.session.add_all([c1, c2, c3])
        db.session.commit()

        imgs_p1 = News_imgs(img_path='/static/imgs/news_1.jpg')
        imgs_p2 = News_imgs(img_path='/static/imgs/Pub_1_.jpg')
        imgs_p3 = News_imgs(img_path='https://mdbootstrap.com/img/Photos/Horizontal/Nature/4-col/img%20(34).jpg')
        imgs_p4 = News_imgs(img_path='/static/imgs/Pub_3.jpg')
        imgs_p5 = News_imgs(img_path='https://mdbootstrap.com/img/Photos/Horizontal/Nature/4-col/img%20(34).jpg')
        imgs_p6 = News_imgs(img_path='/static/imgs/Pub_2.png')
        imgs_p7 = News_imgs(img_path='https://mdbootstrap.com/img/Photos/Horizontal/Nature/4-col/img%20(34).jpg')
        imgs_p8 = News_imgs(img_path='https://mdbootstrap.com/img/Photos/Horizontal/Nature/4-col/img%20(34).jpg')
        imgs_p9 = News_imgs(img_path='/static/imgs/Pub_3.jpg')
        imgs_p10 = News_imgs(img_path='https://mdbootstrap.com/img/Photos/Horizontal/Nature/4-col/img%20(34).jpg')
        imgs_p11 = News_imgs(img_path='/static/imgs/Pub_2.png')
        imgs_p12 = News_imgs(img_path='https://mdbootstrap.com/img/Photos/Horizontal/Nature/4-col/img%20(34).jpg')

        db.session.add_all([imgs_p1, imgs_p2, imgs_p3, imgs_p4])
        db.session.commit()


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
        n1 = News(title=title, category=c1, body=body, intro=intro,
                date=now + timedelta(seconds=1))
        n2 = News(title=title, category=c2, body=body, intro=intro,
                date=now + timedelta(seconds=100))
        n3 = News(title=title, category=c3, body=body, intro=intro,
                date=now + timedelta(seconds=500))
        n4 = News(title=title, category=c2, body=body, intro=intro,
                date=now + timedelta(seconds=1000))
        n5 = News(title=title, category=c1, body=body, intro=intro,
                date=now + timedelta(seconds=1200))
        n6 = News(title=title, category=c2, body=body, intro=intro,
                date=now + timedelta(seconds=1500))
        n7 = News(title=title, category=c3, body=body, intro=intro,
                date=now + timedelta(seconds=2000))
        n8 = News(title=title, category=c2, body=body, intro=intro,
                date=now + timedelta(seconds=2200))
        n9 = News(title=title, category=c1, body=body, intro=intro,
                date=now + timedelta(seconds=2500))
        n10 = News(title=title, category=c2, body=body, intro=intro,
                date=now + timedelta(seconds=3000))
        n11 = News(title=title, category=c3, body=body, intro=intro,
                date=now + timedelta(seconds=3200))
        n12 = News(title=title, category=c2, body=body, intro=intro,
                date=now + timedelta(seconds=3500))

        n1.imgs_dir.append(imgs_p12)
        n2.imgs_dir.append(imgs_p2)
        n3.imgs_dir.append(imgs_p3)
        n4.imgs_dir.append(imgs_p4)
        n5.imgs_dir.append(imgs_p5)
        n6.imgs_dir.append(imgs_p6)
        n7.imgs_dir.append(imgs_p7)
        n8.imgs_dir.append(imgs_p8)
        n9.imgs_dir.append(imgs_p9)
        n10.imgs_dir.append(imgs_p10)
        n11.imgs_dir.append(imgs_p11)
        n12.imgs_dir.append(imgs_p1)


        db.session.add_all([n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11, n12])
        db.session.commit()

def Pub_db():
        pubs = Publications.query.all()
        for u in pubs:
                db.session.delete(u)
        pubs_c = Publication_categories.query.all()
        for u in pubs_c:
                db.session.delete(u)
        pubs_c = Publication_imgs.query.all()
        for u in pubs_c:
                db.session.delete(u)
        pubs_c = Publication_type.query.all()
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

        auth1 = Authors(name='Andrew Peter James', abrev='James A.J.')
        auth2 = Authors(name='Bob Dilan', abrev='Dilan B.')
        auth3 = Authors(name='Oliver Twist', abrev='Oliver T.')
        auth4 = Authors(name='James Goodman', abrev='Goodman J.')

        db.session.add_all([auth1, auth2, auth3, auth4])
        db.session.commit()

        pub_type1 = Publication_type(pub_type='Artigo em Jornal')
        pub_type2 = Publication_type(pub_type='Artigo em Revista')
        pub_type3 = Publication_type(pub_type='Livro')
        pub_type4 = Publication_type(pub_type='Tese')

        db.session.add_all([pub_type1, pub_type2, pub_type3, pub_type4])
        db.session.commit()

        imgs_p1 = Publication_imgs(img_path='/static/imgs/Pub_1_.jpg')
        imgs_p2 = Publication_imgs(img_path='/static/imgs/Pub_2.png')
        imgs_p3 = Publication_imgs(img_path='/static/imgs/Pub_3.jpg')
        imgs_p4 = Publication_imgs(img_path='/static/imgs/Pub_1_.jpg')

        db.session.add_all([imgs_p1, imgs_p2, imgs_p3, imgs_p4])
        db.session.commit()

        intro = '''
                Hyperspectral image classification is an important task in remote sensing image analysis. Traditional machine learning techniques are difficult to deal with hyperspectral images directly, because hyperspectral images have too many redundant spectral channels. In this paper we propose a novel method for hyperspectral image classification, by which spectral and spatial features are jointly exploited from hyperspectral images. Firstly, considering the local similarity in spatial domain, we employ a large spatial window to get image blocks from hyperspectral image Secondly, each spectral channel of the image block is filtered to extract their spatial and spectral features, after that the features are merged by convolutional layers. Finally, the fully-connected layers are used to get the classification result. Comparing with other state-of-the-art techniques, the proposed method pays more attention to the correlation of spatial neighborhood by using a large spatial window in the network. In addition, we combine the proposed network with the traditional support vector machine (SVM) classifier to improve the performance of hyperspectral image classification. Moreover, an adaptive method of the spatial window sizes selection is proposed in this paper. Experimental results conducted on the AVIRIS and ROSIS datasets demonstrate that the proposed method outperforms the state-of-the-art techniques.
                '''

        title = 'Titulo Publicação1 Titulo Publicação Titulo Publicação Titulo Publicação Titulo Publicação'.decode('utf-8')

        now = datetime.utcnow()
        p1 = Publications(title=title, category=c1, file_dir='/static/pdf/pub_ex.pdf', abstract=intro,
                date=now + timedelta(seconds=1), pub_type=pub_type1)
        p2 = Publications(title=title, category=c2, file_dir='/static/pdf/pub_ex.pdf', abstract=intro,
                date=now + timedelta(seconds=1000), pub_type=pub_type2)
        
        p3 = Publications(title=title, category=c3, file_dir='/static/pdf/pub_ex.pdf', abstract=intro,
                date=now + timedelta(seconds=10000), pub_type=pub_type3)

        p4 = Publications(title=title, category=c1, file_dir='/static/pdf/pub_ex.pdf', abstract=intro,
                date=now + timedelta(seconds=20000), pub_type=pub_type1)

        p1.authors.append(auth1)
        p1.authors.append(auth2)
        p1.authors.append(auth3)
        p1.authors.append(auth4)
        p2.authors.append(auth2)
        p2.authors.append(auth3)
        p2.authors.append(auth4)
        p3.authors.append(auth1)
        p3.authors.append(auth4)
        p4.authors.append(auth1)

        p1.imgs_dir.append(imgs_p1)
        p2.imgs_dir.append(imgs_p2)
        p3.imgs_dir.append(imgs_p3)
        p4.imgs_dir.append(imgs_p4)

        db.session.add_all([p1, p2, p3, p4])
        db.session.commit()

     
def Team_db():
        team = Team.query.all()
        for u in team:
                db.session.delete(u)
        db.session.commit()
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
Pub_db()
Team_db()
