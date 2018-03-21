from datetime import datetime
from app import db

class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), index=True, unique=True)
    category = db.Column(db.Integer, db.ForeignKey('news_categories.id'))
    date = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    intro = db.Column(db.String(512))
    body = db.Column(db.Text())

    def index_news():
        return News.query.order_by(News.date.desc()).limit(3)

    def get_cat(self):
        return News_categories.query.filter_by(id=self.category).first().category
    def __repr__(self):
        return '<News {}>'.format(self.title)    

class News_categories(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(64), unique=True)

    def cat_id(category):
        return News_categories.query.filter_by(category=category).first().id

    def __repr__(self):
        return '<News_Category {}>'.format(self.category)    

class Publications(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256), index=True, unique=True)
    category = db.Column(db.Integer, db.ForeignKey('publication_categories.id'))
    date = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    abstract = db.Column(db.Text())
    file_dir = db.Column(db.String(256))
    authors = db.relationship('Publication_authors', backref='publication', lazy='dynamic')

    def index_pubs():
        return Publications.query.order_by(Publications.date.desc()).limit(3)

    def get_cat(self):
        return Publications_categories.query.filter_by(id=self.category).first().category

    def __repr__(self):
        return '<Publication {}>'.format(self.title)    

class Publication_categories(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(64), unique=True)

    def cat_id(category):
        return Publication_categories.query.filter_by(category=category).first().id

    def __repr__(self):
        return '<Publication_Category {}>'.format(self.category)    

class Authors(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256))
    abrev = db.Column(db.String(64))
    publications = db.relationship('Publication_authors', backref='author', lazy='dynamic')
    
    def __repr__(self):
        return '<Author {}>'.format(self.name)  

class Publication_authors(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pub_id = db.Column(db.Integer, db.ForeignKey('publications.id'))
    auth_id = db.Column(db.Integer, db.ForeignKey('authors.id'))
    
    def __repr__(self):
        return '<Pub_author {}>'.format(self.pub_id)  
