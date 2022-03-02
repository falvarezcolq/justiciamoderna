""" Regions Roles """
from django.db import models
from django.utils.translation import ugettext_lazy as _
from justiciamoderna.utils.models import BaseModel
from django_countries.fields import CountryField

class Region(BaseModel):
    name = models.CharField(max_length=64)
    country = CountryField(default=None)







