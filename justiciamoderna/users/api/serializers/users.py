""" User serializers."""
# Django
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import authenticate

# Django REST Framework
from rest_framework import serializers,exceptions
# from rest_framework.serializers import ValidationError


# Models
from justiciamoderna.users.models import User
# from users.models.permission_app import PermissionApp
# import datetime
# from datetime import timedelta

# Serializers
from .data import USER_FIELDS
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework_simplejwt.serializers import TokenObtainSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from datetime import timedelta


class UserModelSerializer(serializers.ModelSerializer):

    """User model serializer"""
    class Meta:
        model = User
        fields = USER_FIELDS



class TokenObtainPairSerializer(TokenObtainSerializer):
    """This serializer return access token and refresh token"""
    username_field = User.USERNAME_FIELD

    default_error_messages = {
        'no_active_account': _('No active account found with the given credentials')
    }

    def validate_credentials(self, attrs):
        authenticate_kwargs = {
            self.username_field: attrs[self.username_field],
            'password': attrs['password'],
        }
        try:
            authenticate_kwargs['request'] = self.context['request']
        except KeyError:
            pass

        self.user = authenticate(**authenticate_kwargs)

        if self.user is None or not self.user.is_active:
            raise exceptions.AuthenticationFailed(
                self.error_messages['no_active_account'],
                'no_active_account',
            )

        return {}


    @classmethod
    def get_token(cls, user):
        """Return token with user's credentials"""
        refresh_token = RefreshToken.for_user(user)
        return refresh_token

    def validate(self, attrs):
        data = self.validate_credentials(attrs)
        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        access = refresh.access_token
        access.set_exp(lifetime=timedelta(days=1))
        data['access'] = str(access)
        # data['access'] = str(refresh.access_token)
        # UserActivityLog.objects.create(
        #     user=self.user,
        #     login_date=datetime.datetime.utcnow(),
        # )
        return data


class UserCompleteModelSerializer(serializers.ModelSerializer):

    # picture =  serializers.SerializerMethodField()
    # permissions = serializers.SerializerMethodField()

    # def get_picture(self,obj):
    #     qs = obj.pictures.filter(is_current_profile_picture=True)
    #     if qs.exists():
    #         return UserPictureSerializer(qs[0]).data
    #     else:
    #         return None
    # def get_permissions(self,obj):
    #     return PermissionApp.ROLS[obj.rol]

    class Meta:
        model = User
        fields = USER_FIELDS + [
            # 'psicture',
            # 'permissions'
           ]


