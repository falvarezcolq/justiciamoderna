"""Lawyer model"""
from django.db import models
from justiciamoderna.utils.models import BaseModel
from .users import User
from .areas import Area
from justiciamoderna.regions.models import Region


class Lawyer(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="lawyer")
    matricula = models.CharField("Matricula",max_length=32,blank=True)
    region = models.ForeignKey(Region,on_delete=models.SET_NULL,null=True,default=None)

    areas = models.ManyToManyField(Area)

    def __str__(self):
        return self.user.name
