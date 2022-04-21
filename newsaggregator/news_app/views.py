from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import requests


# Create your views here.
def index(req):
    return HttpResponse("Hello, world. You're at the news index.")

# get request to newsapi.org

def get_news(req):
    q = req.GET.get('q', '')
    API_KEY = '329db4fb718c407a8f394f328015ea57'
    if q == '':
        get_url = f'https://newsapi.org/v2/top-headlines?apiKey={API_KEY}&category=general&language=en'
    else:
        get_url = f'https://newsapi.org/v2/top-headlines?apiKey={API_KEY}&category=general&language=en&q={q}'

    
    response = requests.get(get_url)
    response = response.json()

    #seperate articles from response
    articles = response['articles']

    #create empty list to store headline, url and source
    headlines = []
    urls = []
    sources = []

    #loop through articles and append to empty list
    for article in articles:
        headlines.append(article['title'])
        urls.append(article['url'])
        sources.append(article['source']['name'])
    
    #create collection to store headlines, urls and sources
    news_collection = zip(headlines, urls, sources)

    response = {
        'news_collection': news_collection
    }

    return render(req, 'index.html', response)
