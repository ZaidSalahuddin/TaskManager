from django.shortcuts import render
from .models import Name

# Create your views here.
def formPageView(request):
    return render(request, "form.html")

def listNamesPageView(request) :
     
    if request.method == 'POST':
        new_vet = Name()
        new_vet.first_name = request.POST.get("firstname")
        new_vet.last_name = request.POST.get("lastname")
        new_vet.save()
    
    data = Name.objects.all()
    context = {"names": data}
    return render(request, "listnames.html", context)

def addNamePageView(request) :
   return render(request, "addname.html")