"""Area model"""

# Django
from django.db import models
from django.utils.translation import ugettext_lazy as _
# Models
# from justiciamoderna.users.models import Lawyer

# UTILS
from justiciamoderna.utils.models import BaseModel

class Area(BaseModel):
    name = models.CharField(_("Law Area") , max_length=128)
    # """ADD MANY TO MANY LAWYERS"""
    # lawyers = models.ManyToManyField(Lawyer,through='LawyerArea')

    def __str__(self):
        return "%s" % (str(self.name),)


# class LawyerArea(BaseModel):
#     area = models.ForeignKey(Area,on_delete=models.CASCADE)
#     lawyer = models.ForeignKey(Lawyer,on_delete=models.CASCADE)

