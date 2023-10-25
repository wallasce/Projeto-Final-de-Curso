from django.shortcuts import render
from .models import HelpContent

# Create your views here.
def homePage(request):
    return render(request, "ContentPage/home.html")

def helpPage(request):
    helpContent = HelpContent.objects.all()
    
    parameters = {
        "contents" : helpContent,
    }
    return render(request, "ContentPage/help.html", parameters)