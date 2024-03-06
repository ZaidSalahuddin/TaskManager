from django.shortcuts import render
from .models import Name

# Create your views here.
def formPageView(request):
    return render(request, "form.html")

def listNamesPageView(request) :
	data = Name.objects.all()
	context = {"names": data}
	return render(request, "listnames.html", context)