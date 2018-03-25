from datetime import datetime
from sqlalchemy import func
from sqlalchemy.ext.hybrid import hybrid_property
from slugify import slugify
from flask import url_for
import re
from app import db

class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), index=True)
    category_id = db.Column(db.Integer, db.ForeignKey('news_categories.id'))
    category = db.relationship('News_categories', backref='news')
    date = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    intro = db.Column(db.String(512))
    body = db.Column(db.Text())
    imgs_dir = db.relationship('News_imgs', backref='news', lazy='dynamic')

    @property
    def slugified_title(self):
        return slugify(self.title)

    def link(self):
        return url_for('news_detail', post_id=self.id, slug=self.slugified_title)

    def __repr__(self):
        return '<News {}>'.format(self.title)    

class News_categories(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(64), unique=True)

    def __repr__(self):
        return '<News_Category {}>'.format(self.category) 

class News_imgs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    new_id = db.Column(db.Integer, db.ForeignKey('news.id'))
    img_path = db.Column(db.String(512))

    def __repr__(self):
        return '<PNews_imgs {}>'.format(self.img_path) 


pub_authors = db.Table('pub_authors',
    db.Column('pub_id', db.Integer, db.ForeignKey('publications.id')),
    db.Column('auth_id', db.Integer, db.ForeignKey('authors.id'))
)  

class Publications(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256), index=True)
    category_id = db.Column(db.Integer, db.ForeignKey('publication_categories.id'))
    category = db.relationship('Publication_categories', backref='publication')
    pub_type_id = db.Column(db.Integer, db.ForeignKey('publication_type.id'))
    pub_type = db.relationship('Publication_type', backref='publication')
    date = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    update = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    abstract = db.Column(db.Text())
    file_dir = db.Column(db.String(512))
    authors = db.relationship('Authors', secondary=pub_authors, backref='publication', lazy='dynamic')
    imgs_dir = db.relationship('Publication_imgs', backref='publication', lazy='dynamic')
    
    @property
    def slugified_title(self):
        return slugify(self.title)

    def link(self):
        return url_for('pubs_detail', post_id=self.id, slug=self.slugified_title)

    def get_cat(self):
        return Publication_categories.query.filter_by(id=self.category).first().category
    
    def __repr__(self):
        return '<Publication {}>'.format(self.title)    

class Publication_categories(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(64), unique=True)

    def cat_id(category):
        return Publication_categories.query.filter_by(category=category).first().id

    def __repr__(self):
        return '<Publication_Category {}>'.format(self.category)    

class Publication_imgs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pub_id = db.Column(db.Integer, db.ForeignKey('publications.id'))
    img_path = db.Column(db.String(512))

    def __repr__(self):
        return '<Publication_imgs {}>'.format(self.img_path) 

class Publication_type(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pub_type = db.Column(db.String(512))

    def __repr__(self):
        return '<Publication_type {}>'.format(self.pub_type) 

class Authors(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256))
    abrev = db.Column(db.String(64))
    
    def __repr__(self):
        return '<Author {}>'.format(self.name)  

class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), index=True, unique=True)
    role = db.Column(db.String(128))
    intro = db.Column(db.Text())
    foto = db.Column(db.String(256))

    def __repr__(self):
        return '<Team {} - {}>'.format(self.name, self.role)    