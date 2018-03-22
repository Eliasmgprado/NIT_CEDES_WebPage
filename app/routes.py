from flask import render_template, flash, redirect, url_for, request
from app import app
from app.models import News, Publications

@app.route('/')
@app.route('/index')
def index():
    news = News.query.order_by(News.date.desc()).limit(3).all()
    publications = Publications.query.order_by(Publications.date.desc()).limit(3)
    return render_template('index.html', news=news, publications=publications)