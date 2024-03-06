from django.urls import path
from .views import formPageView, listNamesPageView, addNamePageView

urlpatterns = [
    path("", formPageView, name="form"),
    path("listnames", listNamesPageView, name="names"),
    path("addnames", addNamePageView, name="addname")
]