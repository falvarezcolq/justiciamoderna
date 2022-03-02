""" ProfilePicture model """

# Django
from django.db import models
from django.utils.translation import ugettext_lazy as _
# Models
from justiciamoderna.users.models import User
# Utils
from justiciamoderna.utils.models import BaseModel,ImageModel
# from justiciamoderna.utils.image_helper import ImageHelper


class ProfilePicture(ImageModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuario",related_name="profilepictures")
    is_current_profile_picture = models.BooleanField(_("current_profile picture"), default=True)

    class Meta:
        verbose_name = "Foto de Perfil"
        verbose_name_plural = "Fotos de Perfil"

    def __str__(self):
        return "%s %s %s" % (self.user, self.is_current_profile_picture)


class RUNPicture(ImageModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="runpictures",related_name="runpictures")
    status = models.BooleanField(_("current_profile picture"), default=True)

    class Meta:
        verbose_name = "RUN imagen"
        verbose_name_plural = "Run imagenes"

    def __str__(self):
        return "%s %s %s" % (self.user, self.status)


class MatriculaPicture(ImageModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="matriculapictures",related_name="matriculapictures")
    status = models.BooleanField(_("current_profile picture"), default=True)

    class Meta:
        verbose_name = "Foto de Perfil"
        verbose_name_plural = "Fotos de Perfil"

    def __str__(self):
        return "%s %s %s" % (self.user, self.status)

