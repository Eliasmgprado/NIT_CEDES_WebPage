from app import app, db
from app.models import News, News_categories, Publications, Publication_categories, Authors, Team

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'News': News, 'News_categories': News_categories,
    'Publications': Publications, 'Publication_categories': Publication_categories, 
    'Authors': Authors, 'Team': Team}