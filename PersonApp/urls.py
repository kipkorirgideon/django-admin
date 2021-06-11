from django.urls import path, include
from PersonApp.views import PersonViewSets
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r"person", PersonViewSets, basename="person")
urlpatterns = [
    path("api/", include(router.urls))
]
