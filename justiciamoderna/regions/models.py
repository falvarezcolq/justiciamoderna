""" Permisions Roles """
from django.db import models
from django.utils.translation import ugettext_lazy as _
from justiciamoderna.utils.models import BaseModel


class Region(BaseModel):
    name = models.CharField(max_length=64)



