from django.db import models

# Create your models here.

class NewsModel(models.Model):
    Title=models.CharField(max_length=150)
    Author=models.CharField(max_length=15)
    Post=models.CharField(max_length=150)

    def __str__(self):
        return str(self.id)+'|' +str(self.Title)