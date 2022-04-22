# News-Aggregator

This solution is a news aggregator built using the Django Framework in Python. To aggregate the news from two different sources, external APIs for NewsAPI and Reddit have been used.

To run the application, you need to install the dependencies and run the following commands in the top-most directory of the project:

## First time setup
```
$ python manage.py makemigrations news_app
$ python manage.py migrate
```

## Run the server
```
$ python manage.py runserver
```

## API Endpoints
Once the server is up and running, the application can be accessed at the following base URL:

```
localhost:8000/news/
```

For accessing the search and list functionality for Part I & II, the following endpoints are available:

```
localhost:8000/news/get_news/ - Get Latest News
localhost:8000/news/get_news?q=<query> - Search News
```
The latencies for the initial requests are noticeably longer than subsequent queries at the same endpoint, as the news are fetched from the external APIs.
Later hits on the same endpoint are cached for a period of time (1 day by default).

## Additional Items
To better visualize the results of the news aggregator, we serve an HTML page with the results. The HTML page contains container elements with hyperlinks for each article returned from the API query.
