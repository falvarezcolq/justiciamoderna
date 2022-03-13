from django.contrib.auth.models import AbstractUser
from django.db.models import CharField,ForeignKey,SET_NULL,CASCADE,BooleanField,EmailField,DateField
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from justiciamoderna.rols.models import Rol,PermissionApp
from justiciamoderna.utils.models import BaseModel



class User(AbstractUser,BaseModel):
    PASSED = 'A'
    REJECTED = 'R'
    PENDING = 'P'
    REVIEW_CHOICES = [
        (PASSED, "PASSED"),
        (REJECTED, "REJECTED"),
        (PENDING, "PENDING"),
    ]
    email = EmailField(unique=True)
    name = CharField(_("Name of User"), blank=True, max_length=255)
    run = CharField(_("RUN of User"), blank=True, max_length=32)
    birth_date = DateField(_("Birth date"))
    cellphone = CharField(_("cellphone of User"), blank=True, max_length=32)
    telephone = CharField(_("Telfone of User"), blank=True, max_length=32)
    address = CharField(_("addresss"),blank=True,max_length=255)
    need_update_profile = BooleanField(default=False)
    reviewed_by_admin = CharField(_("Reviewed by Admin"),max_length=2,choices=REVIEW_CHOICES)
    rol = ForeignKey( Rol, on_delete=SET_NULL, related_name="users", null=True)
    # username= CharField(_("username"), blank=True, max_length=255,unique=True,default="")

    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = ['username','birth_date']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})


class UserPermission(BaseModel):

    user = ForeignKey(User,on_delete=CASCADE,related_name="permissions")
    rol = ForeignKey(Rol,on_delete=SET_NULL,null=True,related_name="user_permissions")
    permission = CharField(max_length=3,choices=PermissionApp.LIST_OF_PERMISSIONS)
    state = BooleanField(default=True)

    class Meta:
        unique_together = (("user", "permission"),)

