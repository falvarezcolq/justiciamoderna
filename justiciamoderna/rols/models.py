""" Permisions Roles """
from django.db import models
from django.utils.translation import ugettext_lazy as _
from justiciamoderna.utils.models import BaseModel

class PermissionApp():
    ADMIN_ACCESS = "A01"
    USER_CREATE_ADMIN = "U02"
    USER_CREATE_LAWYER = "U03"
    USER_CREATE_CUSTOMER = "U04"
    USER_LOGIN = "U05"

    PERMISSIONS = {
        ADMIN_ACCESS : "Admin:Access",
        USER_CREATE_ADMIN : "User:CreateAdmin",
        USER_CREATE_LAWYER : "User:CreateLawyer",
        USER_CREATE_CUSTOMER : "User:CreateCustomer",
        USER_LOGIN :"User:Login",
    }
    LIST_OF_PERMISSIONS = [
        (ADMIN_ACCESS, "Admin:Access"),
        (USER_CREATE_ADMIN, "User:CreateAdmin"),
        (USER_CREATE_LAWYER, "User:CreateLawyer"),
        (USER_CREATE_CUSTOMER, "User:CreateCustomer"),
        (USER_LOGIN, "User:Login"),
    ]



class Rol(BaseModel):
    name = models.CharField(max_length=64)


class RolPermission(BaseModel):
    rol = models.ForeignKey(Rol,on_delete=models.CASCADE,related_name="permissions")
    permission = models.CharField(max_length=3,choices=PermissionApp.LIST_OF_PERMISSIONS)
    state = models.BooleanField(default=True)

    class Meta:
        unique_together = (("rol", "permission"),)



