from django.contrib.auth.models import AbstractUser
from django.db.models import CharField,ForeignKey,SET_NULL,CASCADE,BooleanField,EmailField
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from justiciamoderna.rols.models import Rol,PermissionApp
from justiciamoderna.utils.models import BaseModel



class User(AbstractUser,BaseModel):


    email = EmailField(unique=True)
    name = CharField(_("Name of User"), blank=True, max_length=255)
    dni = CharField(_("DNI of User"), blank=True, max_length=32)
    cellphone = CharField(_("cellphone of User"), blank=True, max_length=32)
    telephone = CharField(_("Telfone of User"), blank=True, max_length=32)
    address = CharField(_("addresss"),blank=True,max_length=255)
    need_update_profile = BooleanField(default=False)
    reviewed_by_admin = BooleanField(default=False)
    rol = ForeignKey( Rol, on_delete=SET_NULL, related_name="users", null=True)

    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = []

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})


class UserPermission(BaseModel):

    user = ForeignKey(User,on_delete=CASCADE,related_name="permissions")
    rol = ForeignKey(Rol,on_delete=SET_NULL,null=True,related_name="user_permissions")
    permission = CharField(max_length=3,choices=PermissionApp.LIST_OF_PERMISSIONS)
    state = BooleanField(default=True)

    class Meta:
        unique_together = (("user", "permission"),)

