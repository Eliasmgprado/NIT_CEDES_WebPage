from flask import render_template, flash, redirect, url_for, request, abort, send_from_directory
from app import app
from slugify import slugify
from app.models import News, Publications, Team
import os

@app.route('/')
@app.route('/CPRM.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'CPRM.ico', mimetype='image/png')
@app.route('/index')
def index():
    news = News.query.order_by(News.date.desc()).limit(3).all()
    publications = Publications.query.order_by(Publications.date.desc()).limit(3)
    team = Team.query.order_by(Team.role.desc())
    return render_template('index.html', news=news, publications=publications, team=team)

@app.route('/news')
def news():
    page = request.args.get('page', 1, type=int)
    news = News.query.order_by(News.date.desc()).paginate(page, app.config['POSTS_PER_PAGE'], False)

    next_url = url_for('news', page=news.next_num) \
        if news.has_next else None
    prev_url = url_for('news', page=news.prev_num) \
        if news.has_prev else None
    return render_template('news.html', page=page, news=news, next_url=next_url, prev_url=prev_url)

@app.route('/news/<slug>-<post_id>')
def news_detail(slug, post_id):
    new = News.query.filter_by(id=post_id).first_or_404()
    if not slugify(new.title) == slug:
        abort(404)
    return render_template('new.html', new=new)
