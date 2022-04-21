from django.db import models

# Create your models here.
class News(models.Model):
    news_json = models.TextField()
    source = models.CharField(max_length=100)
    saved_at_date = models.DateField()
    parameters = models.TextField()