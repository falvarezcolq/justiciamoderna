"""Django models utilities."""

# Django
from django.db import models
from django.utils.translation import ugettext_lazy as _
from .image_helper import ImageHelper

class BaseModel(models.Model):
    """Base model.

    BaseModel acts as an abstract base class from which every
    other model in the project will inherit. This class provides
    every table with the following attributes:
        + created (DateTime): Store the datetime the object was created.
        + modified (DateTime): Store the last datetime the object was modified.
    """
    created = models.DateTimeField(
        'created at',
        auto_now_add=True,
        help_text='Date time on which the object was created.'
    )
    modified = models.DateTimeField(
        'modified at',
        auto_now=True,
        help_text='Date time on which the object was last modified.'
    )

    class Meta:
        """Meta option."""

        abstract = True
        get_latest_by = 'created'
        ordering = ['-created', '-modified']


class ImageModel(models.Model):
    img_l = models.ImageField(_("picture size large 1024x1024"), max_length=255, null=True, upload_to="x/x1")
    img_m = models.ImageField(_("picture size medium 400x400"), max_length=255, null=True, default="", upload_to="x/x5")
    thumbnail = models.ImageField(_("picture size small 70x70"), max_length=255, null=True, default="", upload_to="x/x4")
    created = models.DateTimeField(
        'created at',
        auto_now_add=True,
        help_text='Date time on which the object was created.'
    )
    modified = models.DateTimeField(
        'modified at',
        auto_now=True,
        help_text='Date time on which the object was last modified.'
    )

    def __str__(self):
        return "%s" % (self.img_l,)

    class Meta:
        """Meta option."""
        abstract = True


    def save(self, *args, **kwargs):
        # import pdb;pdb.set_trace()

        imagesave = ImageHelper()
        self.img_l = imagesave.compressImage(self.img_l, 1280, 1280, 50)
        self.img_m = imagesave.compressImage(self.img_l, 400, 400, 50)
        self.thumbnail = imagesave.compressImage(self.img_l, 100, 100, 50)

        super(ImageModel, self).save(*args, **kwargs)
