from django.shortcuts import render

# Create your views here.
def formPageView(request):
    return render(request, "form.html")