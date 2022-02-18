"""Lawyer model"""
from django.db import models
from justiciamoderna.utils.models import BaseModel
from .users import User

class Lawyer(BaseModel):
    user = models.OneToOneRel(User,on_delete=models.CASCADE,related_name="lawyer")
    matricula = models.CharField("Matricula",max_length=32)
