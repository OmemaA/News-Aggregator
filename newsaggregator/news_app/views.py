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

# get request to newsapi.org

def get_news(req):
    q = req.GET.get('q', '')

    API_KEY = '329db4fb718c407a8f394f328015ea57'
    
    reddit = praw.Reddit(
    client_id= "JOMVkfinUF2r6p2niNo1fA",
    client_secret= "JRUg34esT_xxDoXWnHLwEbVCCc9uDQ",
    user_agent="win32:test_stellic_app:0.1.0 (by /u/Mindreader03")
    # print(reddit.read_only)

    #create empty list to store headline, url and source
    headlines, urls, sources = [], [], []

    if q == '':
        news_collection = News.objects.filter(parameters='today')
        print(news_collection.values())
        if not news_collection.exists():
            # for NewsAPI
            get_url = f'https://newsapi.org/v2/top-headlines?apiKey={API_KEY}&category=general&language=en'
            response = requests.get(get_url)
            response = response.json()
            # seperate articles from response
            articles = response['articles']
            # loop through articles and append to empty list
            for article in articles:
                headlines.append(article['title'])
                urls.append(article['url'])
                sources.append('newsapi')
                # sources.append(article['source']['name'])

            # for Reddit
            for article in reddit.subreddit('news').hot():
                headlines.append(article.title)
                urls.append(article.url)
                sources.append('reddit')
            # create collection to store headlines, urls and sources
            news_collection = zip(headlines, urls, sources)
            # save to database
            headlines = str(headlines)
            urls = str(urls)
            sources = str(sources)

            # articles = News(parameters='today', headline = str(headlines), urls = str(urls), source = str(sources), saved_at_date = datetime.date.today)
            articles = News(parameters='today', headline = headlines, urls = urls, source = sources, saved_at_date = datetime.date.today)
            articles.save()
        else:
            news_collection = list(news_collection)
            print(news_collection)


    else:
        news_collection = News.objects.filter(parameters = q)
        if not news_collection.exists():
            # for NewsAPI
            get_url = f'https://newsapi.org/v2/top-headlines?apiKey={API_KEY}&category=general&language=en&q={q}'
            response = requests.get(get_url)
            response = response.json()
            # seperate articles from response
            articles = response['articles']
            # loop through articles and append to empty list
            for article in articles:
                headlines.append(article['title'])
                urls.append(article['url'])
                sources.append('newsapi')
                # sources.append(article['source']['name'])
            # for Reddit
            all = reddit.subreddit("news")
            for article in all.search(q):
                headlines.append(article.title)
                urls.append(article.url)
                sources.append('reddit')
            # create collection to store headlines, urls and sources
            news_collection = zip(headlines, urls, sources)
            # save to database
            articles = News(parameters='today', headline = str(headlines), urls = str(urls), source = str(sources), saved_at_date = datetime.date.today)
            articles.save()
            
    # response = {
    #     'news_collection': news_collection
    # }


    # return render(req, 'index.html', response)
    return HttpResponse("Hello, world. You're at the news index.")
