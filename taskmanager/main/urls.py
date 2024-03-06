from django.urls import path
from .views import *

urlpatterns = [
    path("", formPageView, name="form"),
    path("listnames", listNamesPageView, name="names"),
    path("addnames", addNamePageView, name="addname"),
    path("editname/<int:iNameID>", editNamePageView, name="editname"),
    path("deletename/<int:iNameID>", deleteNamePageView, name="deletename")
]