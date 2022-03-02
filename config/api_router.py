from django.urls import include, path
app_name = "api"
urlpatterns = [
    path("", include("justiciamoderna.users.api.urls")),
    path("",include("justiciamoderna.regions.urls")),

]
