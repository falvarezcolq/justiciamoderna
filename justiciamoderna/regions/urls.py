from rest_framework.routers import DefaultRouter, SimpleRouter
from django.conf import settings
from django.urls import path
from .views import RegionViewSet,CountryView

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("regions", RegionViewSet)
app_name = "api"

urlpatterns = [
  path('countries/', CountryView.as_view(), name="countries"),
] + router.urls
