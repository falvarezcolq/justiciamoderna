from rest_framework.routers import DefaultRouter, SimpleRouter
from django.conf import settings
from .views.users import TokenObtainPairView,UserViewSet,DataSessionApiView
from rest_framework_simplejwt.views import TokenRefreshView
from django.urls import path


if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)


app_name = "api"
urlpatterns = [
  path('auth/login/', TokenObtainPairView.as_view(), name="gettoken"),
  path('auth/refresh/', TokenRefreshView.as_view(), name="refreshtoken"),
  path('auth/datasession/', DataSessionApiView.as_view(),name="datasession"),
] + router.urls
