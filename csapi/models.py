from django.db import models

class Country(models.Model):
    id = models.IntegerField()
    code = models.CharField(max_length=2)
    name = models.CharField(max_length=60)

class State(models.Model):
    id = models.IntegerField()
    country_id = models.IntegerField()
    code = models.CharField(max_length=2)
    name = models.CharField(max_length=60)

