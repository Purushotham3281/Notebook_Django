from django.db import models

# Create your models here.
class Notes(models.Model):
    Title=models.CharField(max_length=50)
    Date=models.CharField(max_length=15)
    Description=models.CharField(max_length=10000)


    def __str__(self):
        return self.Title
