from django.shortcuts import render, redirect
from .models import Task

# Create your views here.
def listTasksPageView(request) :
     
    if request.method == 'POST':
        new_task = Task()
        new_task.name = request.POST.get("name")
        new_task.description = request.POST.get("description")
        new_task.save()
    
    data = Task.objects.all()
    context = {"names": data}
    return render(request, "listtasks.html", context)

def addTaskPageView(request) :
   return render(request, "addtask.html")

def deleteTaskPageView(request, iTaskID):
    Task.objects.get(id=iTaskID).delete()
    return redirect(listTasksPageView)

def editTaskPageView(request, iTaskID) :
   name = Task.objects.get(id=iTaskID)
   # if updating from from post, do this if statement
   if request.method == 'POST':
       # put the update code here, then redirect to view.
       name.name = request.POST.get("name")
       name.description = request.POST.get("description")
       name.save()
       #redirect to display veterinarian page if this was an update
       return redirect(listTasksPageView)

   context = {
       "name": name
   }
   return render(request, "edittask.html", context)