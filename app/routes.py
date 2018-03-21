from flask import render_template, flash, redirect, url_for, request
from app import app
from app.models import News, Publications

@app.route('/')
@app.route('/index')
def index():
    news = News.index_news().all()
    publications = Publications.index_pubs().all()
    return render_template('index.html', news=news, publications=publications)