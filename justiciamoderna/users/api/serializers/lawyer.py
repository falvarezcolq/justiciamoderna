"""Lawyer Serializer"""
# Django
from django.utils.translation import ugettext_lazy as _

# Django REST Framework
from rest_framework import serializers,exceptions
from rest_framework.serializers import ValidationError


# models
from justiciamoderna.users.models import User,Profile,Lawyer,UserPermission
from justiciamoderna.rols.models import Rol,RolPermission,PermissionApp
from justiciamoderna.regions.models import Region
from justiciamoderna.regions.serializers import RegionModelSerializer

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
    birth_date = serializers.DateField(required=True)
    cellphone = serializers.CharField(  max_length=32)
    telephone = serializers.CharField(  max_length=32)
    address = serializers.CharField(  max_length=255)
    matricula = serializers.CharField(min_length=6,max_length=32,allow_blank=True
                                      # validators=[UniqueValidator(queryset=Lawyer.objects.all())]
                                      )
    region = serializers.IntegerField()

    def validate_region(self,data):
        try:
            region = Region.objects.get(pk=data)
        except Region.DoesNotExist:
            raise ValidationError(_("Region does not exists"))
        return region

    def validate(self, attrs):
        try:
            self.context['rol'] = Rol.objects.get(name=Rol.LAWYER)
        except Rol.DoesNotExist:
            raise ValidationError(_("Admin has not yet created the rol lawyer"))
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
                                        birth_date = data['birth_date'],
                                        cellphone = data['cellphone'],
                                        telephone = data['telephone'],
                                        address = data['address'],
                                        need_update_profile = True,
                                        rol = self.context['rol'],
                                        reviewed_by_admin = User.PENDING )
        Lawyer.objects.create(
            user=user,
            matricula=data['matricula'],
            region=data['region'],
        )

        UserPermission.objects.create(
            user=user,
            permission=PermissionApp.USER_LOGIN,
            state=True,
        )
        return user


class LawyerModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lawyer
        fields = '__all__'



