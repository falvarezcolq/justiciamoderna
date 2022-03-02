"""Profile picture serializer."""

# Django REST Framework
from rest_framework.serializers import ModelSerializer,HiddenField,CurrentUserDefault,ImageField
from rest_framework.serializers import FileField
# models
from justiciamoderna.users.models.profilepicture import ProfilePicture,RUNPicture,MatriculaPicture


class ProfilePictureSerializer(ModelSerializer):

    user = HiddenField(default=CurrentUserDefault())
    img_l = ImageField(required=True)
    """Profile picture serializer."""
    class Meta:
        model = ProfilePicture
        fields = ('id',
                  'user',
                  'is_current_profile_picture',
                  'img_l',
                  'img_m',
                  'thumbnail',
                  )
        fields_read_only = (
            'is_current_profile_picture',
            'user',
        )

    def create(self, data):
        """Create a new ProfilePicture for user"""
        ModelClass = self.Meta.model
        data['is_current_profile_picture']=True
        ModelClass.objects.filter(user=data['user'],
                                  is_current_profile_picture=True
                                  ).update(is_current_profile_picture=False)
        instance = ModelClass.objects.create(**data)

        return instance




class RUNPictureSerializer(ModelSerializer):
    """RUN picture serializer."""

    user = HiddenField(default=CurrentUserDefault())
    img_l = ImageField(required=True)

    class Meta:
        model = RUNPicture
        fields = ('id',
                  'user',
                  'status',
                  'img_l',
                  'img_m',
                  'thumbnail',
                  )
        fields_read_only = (
            'user',
        )

    def create(self, data):
        """Create a new ProfilePicture for user"""
        ModelClass = self.Meta.model
        data['status']=True
        ModelClass.objects.filter(user=data["user"],
                                  status=True
                                  ).update(status=False)
        instance = ModelClass.objects.create(**data)
        return instance


class MatriculaPictureSerializer(ModelSerializer):
    """RUN picture serializer."""
    user = HiddenField(default=CurrentUserDefault())
    img_l = ImageField(required=True)
    class Meta:
        model = MatriculaPicture
        fields = ('id',
                  'user',
                  'status',
                  'img_l',
                  'img_m',
                  'thumbnail',
                  )
        fields_read_only = (
            'user',
        )

    def create(self, data):
        """Create a new ProfilePicture for user"""
        ModelClass = self.Meta.model
        data['status']=True
        ModelClass.objects.filter(user=data["user"],
                                  status=True
                                  ).update(status=False)
        instance = ModelClass.objects.create(**data)
        return instance



