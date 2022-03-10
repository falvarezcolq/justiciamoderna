"""Lawyer model"""
from django.db import models
from justiciamoderna.utils.models import BaseModel
from .users import User
from justiciamoderna.regions.models import Region

class Lawyer(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="lawyer")
    matricula = models.CharField("Matricula",max_length=32,blank=True)
    region = models.ForeignKey(Region,on_delete=models.SET_NULL,null=True,default=None)
