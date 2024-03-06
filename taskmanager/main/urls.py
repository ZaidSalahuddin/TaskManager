from django.urls import path
from .views import formPageView

urlpatterns = [
    path("", formPageView, name="form")
]