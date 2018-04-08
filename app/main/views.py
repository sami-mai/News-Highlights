from flask import render_template
from . import main
from ..request import get_news

# views

@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    # Get news
    us_headlines = get_news('us')
    au_headlines = get_news('au')
    de_headlines = get_news('de')
    kr_headlines = get_news('kr')

    title = 'Home - Welcome to the best live news website'
    
    return render_template('index.html', title = title, us_news = us_headlines,
    au_news = au_headlines, de_news = de_headlines, kr_news = kr_headlines)
