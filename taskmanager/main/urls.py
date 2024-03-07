from django.urls import path
from .views import *

urlpatterns = [
    path("", listTasksPageView, name="form"),
#    path("listnames", listTasksPageView, name="names"),
    path("addnames", addNamePageView, name="addname"),
    path("editname/<int:iNameID>", editNamePageView, name="editname"),
    path("deletename/<int:iNameID>", deleteNamePageView, name="deletename")
]