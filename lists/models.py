from django.db import models

# Create your models here.
class Item(object):
    text = models.TextField(default='')