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
    category = db.Column(db.Integer, db.ForeignKey('news_categories.id'))
    date = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    intro = db.Column(db.String(512))
    body = db.Column(db.Text())

    @property
    def slugified_title(self):
        return slugify(self.title)

    def link(self):
        return url_for('news_detail', post_id=self.id, slug=self.slugified_title)

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

pub_authors = db.Table('pub_authors',
    db.Column('pub_id', db.Integer, db.ForeignKey('publications.id')),
    db.Column('auth_id', db.Integer, db.ForeignKey('authors.id'))
)  

class Publications(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256), index=True)
    category = db.Column(db.Integer, db.ForeignKey('publication_categories.id'))
    date = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    abstract = db.Column(db.Text())
    file_dir = db.Column(db.String(256))
    authors = db.relationship('Authors', secondary=pub_authors, backref='publication', lazy='dynamic')
    img_dir = db.Column(db.String(256))

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