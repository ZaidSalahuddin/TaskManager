from django.shortcuts import render, redirect
from .models import Task

# Create your views here.
def formPageView(request):
    return render(request, "form.html")

def listTasksPageView(request) :
     
    if request.method == 'POST':
        new_task = Task()
        new_task.name = request.POST.get("name")
        new_task.description = request.POST.get("description")
        new_task.save()
    
    data = Task.objects.all()
    context = {"names": data}
    return render(request, "listnames.html", context)

def addNamePageView(request) :
   return render(request, "login.html")

def deleteNamePageView(request, iNameID):
    Task.objects.get(id=iNameID).delete()
    return redirect(listTasksPageView)

def editNamePageView(request, iNameID) :
   name = Task.objects.get(id=iNameID)
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
   return render(request, "editname.html", context)