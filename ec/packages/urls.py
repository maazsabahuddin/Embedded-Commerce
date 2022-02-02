from django.urls import path

from ec.packages.views import getPackage

app_name = "packages"
urlpatterns = [
    path("", getPackage, name="package"),
]
