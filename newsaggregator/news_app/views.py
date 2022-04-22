from distutils.ccompiler import new_compiler
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from news_app.models import News
import requests
import praw
import datetime

# Create your views here.
def index(req):
    return HttpResponse("Hello, world. You're at the news index.")

def get_news(req):
    q = req.GET.get('q', 'today')
    query_string = '' if q=='today' else f'&q={q}'

    # Initializing APIs
    API_KEY = '329db4fb718c407a8f394f328015ea57'

    reddit = praw.Reddit(
    client_id= "JOMVkfinUF2r6p2niNo1fA",
    client_secret= "JRUg34esT_xxDoXWnHLwEbVCCc9uDQ",
    user_agent="win32:test_stellic_app:0.1.0 (by /u/Mindreader03")

    #create empty list to store headline, url and source
    headlines, urls, sources, news_collection = [], [], [], None

    get_url = f'https://newsapi.org/v2/top-headlines?apiKey={API_KEY}&category=general&language=en' + query_string

    news_collection = News.objects.filter(parameters=q)
    if not news_collection.exists():
        headlines, urls, sources = get_from_API(reddit, q, get_url)
    else:
        date = news_collection.values('saved_at_date')[0]['saved_at_date']
        if date == datetime.datetime.now().strftime("%m/%d/%Y"):
            headlines, urls, sources = get_from_database(news_collection)
        else:
            headlines, urls, sources = get_from_API(reddit, 'today', get_url)
            
    # create collection to store headlines, urls and sources
    news_collection = zip(headlines, urls, sources)
    response = {
        'news_collection': news_collection
    }

    return render(req, 'index.html', response)

def get_from_database(news_collection):
    headlines, urls, sources = [], [], []
    headlines = eval(news_collection.values('headline')[0]['headline'])
    urls = eval(news_collection.values('urls')[0]['urls'])
    sources = eval(news_collection.values('source')[0]['source'])
    return headlines, urls, sources 

def get_from_API(reddit, parameter, get_url):
    headlines, urls, sources = [], [], []
    # for NewsAPI
    response = requests.get(get_url)
    response = response.json()
    # seperate articles from response
    articles = response['articles']
    # loop through articles and append to empty list
    for article in articles:
        headlines.append(article['title'])
        urls.append(article['url'])
        sources.append('newsapi')

    # for Reddit
    for article in reddit.subreddit('news').hot():
        headlines.append(article.title)
        urls.append(article.url)
        sources.append('reddit')
    # save to database
    articles = News(parameters=parameter, headline = str(headlines), urls = str(urls), source = str(sources), saved_at_date = datetime.datetime.now().strftime("%m/%d/%Y"))
    articles.save()
    return headlines, urls, sources 
