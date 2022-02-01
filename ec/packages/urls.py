from django.urls import path

from ec.packages.views import get_package

app_name = "packages"
urlpatterns = [
    path("/", get_package, name="package"),
]
