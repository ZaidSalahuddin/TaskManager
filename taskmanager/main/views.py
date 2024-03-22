from django.shortcuts import render, redirect
from .models import Name

# Create your views here.

def listNamesPageView(request) :
     
    if request.method == 'POST':
        new = Name()
        new.task = request.POST.get("firstname")
        new.description = request.POST.get("lastname")
        new.time_to_complete = request.POST.get("time")
        new.save()
    
    data = Name.objects.all()
    context = {"names": data}
    return render(request, "listnames.html", context)

def addNamePageView(request) :
   return render(request, "addname.html")

def deleteNamePageView(request, iNameID):
    Name.objects.get(id=iNameID).delete()
    return redirect(listNamesPageView)

def editNamePageView(request, iNameID) :
   name = Name.objects.get(id=iNameID)
   # if updating from from post, do this if statement
   if request.method == 'POST':
       # put the update code here, then redirect to view.
       name.task = request.POST.get("firstname")
       name.description = request.POST.get("lastname")
       name.time_to_complete = request.POST.get("time")
       name.save()
       #redirect to display task page if this was an update
       return redirect(listNamesPageView)

   context = {
       "name": name
   }
   return render(request, "editname.html", context)