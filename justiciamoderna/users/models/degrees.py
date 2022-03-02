"""Degree model"""

# Django
from django.db import models
from django.utils.translation import ugettext_lazy as _
# Models
from justiciamoderna.users.models import User
# UTILS
from justiciamoderna.utils.models import ImageModel

class Degree(ImageModel):
    DIPLOMA = "DI"
    TECHNICIAN_DEGREE = "TE" #technician
    COLLEGE_DEGREE = "CO"
    MASTER_DEGREE = "MA"
    DOCTORAL_DEGREE = "DO"
    POST_DOCTORAL_DEGREE = "PD"

    LIST_OF_DEGREE = [
        (DIPLOMA,_("Diploma")),
        (TECHNICIAN_DEGREE, _("Technician degree")),
        (COLLEGE_DEGREE, _("College degree")),
        (MASTER_DEGREE, _("Master's degree")),
        (DOCTORAL_DEGREE, _("Doctoral degree / Doctorate")),
        (POST_DOCTORAL_DEGREE, _("Post Doctoral degree /Post Doctorate")),
    ]

    user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="degree",related_name="degrees")
    university = models.CharField(_("University"),max_length=256)
    career = models.CharField(_("Career"),max_length=256)
    academic_degree = models.CharField(max_length=2,choices=LIST_OF_DEGREE)
