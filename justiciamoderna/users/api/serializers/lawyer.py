"""Lawyer Serializer"""
# Django
from django.utils.translation import ugettext_lazy as _

# Django REST Framework
from rest_framework import serializers,exceptions
from rest_framework.serializers import ValidationError


# models
from justiciamoderna.users.models import User,Profile,Lawyer,UserPermission
from justiciamoderna.rols.models import Rol,RolPermission,PermissionApp
from rest_framework.validators import UniqueValidator

def get_ID_USER():
    INIT = 1000501
    last = 0
    try:
        latest_user = User.objects.latest('id')
        last = latest_user.id
    except User.DoesNotExist:
        pass
    return  str( INIT + last) # Return ID USER

class LawyerCreateSerializer(serializers.Serializer):
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(min_length=8)
    first_name = serializers.CharField(min_length=2,max_length=36)
    last_name = serializers.CharField(min_length=2,max_length=36)
    run = serializers.CharField(max_length=32)
    cellphone = serializers.CharField(  max_length=32)
    telephone = serializers.CharField(  max_length=32)
    address = serializers.CharField(  max_length=255)
    matricula = serializers.CharField(min_length=6,max_length=32,allow_blank=True
                                      # validators=[UniqueValidator(queryset=Lawyer.objects.all())]
                                      )
    region = serializers.IntegerField()


    def validate(self, attrs):
        try:
            self.context['rol'] = Rol.objects.get(name=Rol.LAWYER)
        except Rol.DoesNotExist:
            ValidationError(_("Admin has not yet created the rol lawyer"))
        return attrs



    def create(self,data):
        ID_USER= get_ID_USER()
        name = (data['first_name'] + ' '+data['last_name']).strip()
        user = User.objects.create_user(username=ID_USER,
                                        name=name,
                                        email =data['email'],
                                        password= data['password'],
                                        first_name = data['first_name'],
                                        last_name = data['last_name'],
                                        run = data['run'],
                                        cellphone = data['cellphone'],
                                        telephone = data['telephone'],
                                        address = data['address'],
                                        need_update_profile = True,
                                        rol = self.context['rol'],
                                        reviewed_by_admin = False )
        Lawyer.objects.create(
            user=user,
            matricula=data['matricula']
        )

        UserPermission.objects.create(
            user=user,
            permission=PermissionApp.USER_LOGIN,
            state=True,
        )




        return user









