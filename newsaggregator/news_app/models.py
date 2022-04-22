from django.db import models
from numpy import source

# create your models here.

class News(models.Model):
    # search parameters for articles
    parameters = models.TextField(primary_key=True)
    # JSON object containing all articles for specified parameters
    headline = models.TextField()
    # date of fetch stored to calculate expiry date while searching
    saved_at_date = models.TextField()
    urls = models.TextField()
    source = models.TextField()

    def getSavedDate(self):
        return self.saved_at_date

