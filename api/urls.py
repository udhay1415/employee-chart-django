from django.urls import path, include
from .views import *

urlpatterns = [
  path("ping/", ping),
  path("seed/", seed),
  path("v1/", include("api.v1.urls"))
]