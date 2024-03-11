from django.urls import path
from .views import *

urlpatterns = [
    path("", listTasksPageView, name="tasks"),
#    path("listtasks", listTasksPageView, name="tasks"),
    path("addnames", addTaskPageView, name="addtask"),
    path("editname/<int:iTaskID>", editTaskPageView, name="edittask"),
    path("deletetask/<int:iTaskID>", deleteTaskPageView, name="deletetask")
]