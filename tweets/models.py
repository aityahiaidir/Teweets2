from django.db import models

# Create your models here.


class Tweet(models.Model):
    content = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to='iamges/', blank=True, null=True)
