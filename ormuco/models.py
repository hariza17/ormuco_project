from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

CHOICES = (('Dogs', 'Dogs'),('Cats', 'Cats'),)

class Person(models.Model):
	name = models.CharField(max_length=200)
	favorite_color = models.CharField(max_length=200)
	animal = models.CharField(max_length=200,choices=CHOICES)
# Create your models here.
