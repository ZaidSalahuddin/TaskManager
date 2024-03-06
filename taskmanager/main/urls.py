from django.urls import path
from .views import formPageView, listNamesPageView

urlpatterns = [
    path("", formPageView, name="form"),
    path("listnames", listNamesPageView, name="names")
]