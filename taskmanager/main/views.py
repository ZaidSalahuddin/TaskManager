from django.shortcuts import render, redirect
from .models import Name

# Create your views here.

def listNamesPageView(request) :
     
    if request.method == 'POST':
        new_name = Name()
        new_name.first_name = request.POST.get("firstname")
        new_name.last_name = request.POST.get("lastname")
        new_name.save()
    
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
       name.first_name = request.POST.get("firstname")
       name.last_name = request.POST.get("lastname")
       name.save()
       #redirect to display task page if this was an update
       return redirect(listNamesPageView)

   context = {
       "name": name
   }
   return render(request, "editname.html", context)