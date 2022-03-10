"""Users views"""

# Django

from django.utils.translation import ugettext_lazy as _

# Django REST Framework
from rest_framework import mixins,viewsets,status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.decorators import action
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated,AllowAny


# Django REST Framework JWT

from rest_framework_simplejwt.views import TokenViewBase


# Models
from justiciamoderna.users.models.users import User
from justiciamoderna.users.models.profilepicture import ProfilePicture,RUNPicture,MatriculaPicture

# Utils
# from utils.pagination import CustomPagination
# import jwt, datetime

from justiciamoderna.users.api.serializers import UserModelSerializer,TokenObtainPairSerializer,UserCompleteModelSerializer

from ..serializers.lawyer import LawyerCreateSerializer
from ..serializers.profilepictures import ProfilePictureSerializer,RUNPictureSerializer,MatriculaPictureSerializer
class UserViewSet(mixins.RetrieveModelMixin,
                  mixins.ListModelMixin,
                  # mixins.UpdateModelMixin,
                  # mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):
#     """User viewset """
    queryset =  User.objects.all()
    serializer_class = UserModelSerializer
    # pagination_class = CustomPagination
#     # filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend)
#     # ordering = ('last_name',)
#     # ordering_fields = ('last_name', 'created_at')
#     # search_fields = ('first_name','last_name','last_name2','CI')
#   # filterset_fields = ['type']

    def get_permissions(self):
        """Assign permissions based on action."""

        if self.action in []:
            # 'updateuserpassword',
            # # 'register',
            # 'updateuseraccess',
            # 'destroy', 'log']:
            permissions = [IsAuthenticated, ]
        elif self.action in ['profilepicture']:
            permissions = [IsAuthenticated, ]
        else:
            permissions = [AllowAny]
        return [p() for p in permissions]


    @action(detail=False, methods=['post'])
    def registerlawyer(self,request):
        """ User update password """
        serializer = LawyerCreateSerializer(data=request.data,context={"request":self.request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response_data = {"message": _('user Created')}
        return Response(response_data, status=status.HTTP_200_OK)



    @action(detail=False, methods=['POST','DELETE'])
    def profilepicture(self,request):
        """ User update user picture """
        if request.method == 'DELETE':
            try:
                profilepicture = request.user.profilepictures.get(is_current_profile_picture = True)
                profilepicture.is_current_profile_picture = False
                profilepicture.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
            except ProfilePicture.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)


        serializer = ProfilePictureSerializer(data=request.data,context={'request':self.request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response_data = serializer.data
        return Response(response_data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['POST','DELETE'])
    def runpicture(self,request):
        """ User update user picture """
        if request.method == 'DELETE':
            try:
                runpicture = request.user.runpictures.get(status= True)
                runpicture.status = False
                runpicture.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
            except RUNPicture.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = RUNPictureSerializer(data=request.data,context={'request':self.request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response_data = serializer.data
        return Response(response_data, status=status.HTTP_200_OK)


    @action(detail=False, methods=['POST','DELETE'])
    def matriculapicture(self,request):
        """ User update user picture """
        if request.method == 'DELETE':
            try:
                matriculapicture = request.user.matriculapictures.get(status= True)
                matriculapicture.status = False
                matriculapicture.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
            except MatriculaPicture.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = MatriculaPictureSerializer(data=request.data,context={'request':self.request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response_data = serializer.data
        return Response(response_data, status=status.HTTP_200_OK)


    # @action(detail=False, methods=['post'])
    # def updatepassword(self,request):
    #     """ User update password """
    #     serializer = UpdateMyPasswordSerializer(
    #         data=request.data,
    #         context={"user": request.user})
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     response_data = {
    #         "message": _('password updated')
    #     }
    #     return Response(response_data, status=status.HTTP_200_OK)

    #
    # @action(detail=False, methods=['post'])
    # def updateuserpassword(self, request):
    #     """ User update password """
    #     serializer = UpdatePasswordUserSerializer(
    #         data=request.data,
    #         context={"user": request.user})
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     response_data = {
    #         "message": _('Password Updated')
    #     }
    #     return Response(response_data, status=status.HTTP_200_OK)
    #
    # @action(detail=True, methods=['get','put'])
    # def address(self, request,*args,**kwargs):
    #     """ return user's address"""
    #     if request.method == 'GET':
    #         user = self.get_object()
    #
    #         try:
    #
    #             serializer = AddressModelSerializer(user.user_address)
    #             return Response(serializer.data, status=status.HTTP_200_OK)
    #         except User.user_address.RelatedObjectDoesNotExist:
    #             return Response({"detail": _("user haven't address")}, status=status.HTTP_204_NO_CONTENT)
    #
    #     elif request.method == 'PUT':
    #         user = self.get_object()
    #
    #         try:
    #
    #             serializer = AddressModelSerializer(user.user_address,data=request.data)
    #             serializer.is_valid(raise_exception=True)
    #             serializer.save()
    #             return Response(serializer.data, status=status.HTTP_200_OK)
    #         except User.user_address.RelatedObjectDoesNotExist:
    #             serializer = AddressModelSerializer(data=request.data)
    #             serializer.is_valid(raise_exception=True)
    #             address = Address.objects.create(user=user, **request.data)
    #             return Response( AddressModelSerializer(address).data, status=status.HTTP_200_OK)
    #
    #
    #
    # @action(detail=True, methods=['get'])
    # def log(self, request,*args,**kwargs):
    #     """ return user's address"""
    #     user = self.get_object()
    #     data = UserActivityLogModelSerializer(user.logs.order_by('-id'),many=True).data
    #     return Response(data, status=status.HTTP_200_OK)
    #
    #
    # @action(detail=True, methods=['post'])
    # def state(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     serializer = UserStateSerializer(instance,
    #                                      data=request.data,
    #                                      context={'request': self.request})
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     data = UserModelSerializer(instance).data
    #     return Response(data)
    #
    # @action(detail=True,methods=['get'])
    # def profile(self,request,*args,**kwargs):
    #     user = self.get_object()
    #     data = UserWithPictureModelSerializer(user).data
    #     return Response(data, status=status.HTTP_200_OK)

class TokenObtainPairView(TokenViewBase):
    """
    API LOGIN
    return access_token and refresh token

    Takes a set of user credentials and returns an access and refresh JSON web
    token pair to prove the authentication of those credentials.
    """
    serializer_class = TokenObtainPairSerializer


class DataSessionApiView(RetrieveAPIView):
    """
    API DATA SESSION
    RETURN data for storage front
    """
    permission_classes = [
        IsAuthenticated,
    ]
    serializer_class = UserCompleteModelSerializer

    def get_object(self):
        return self.request.user
