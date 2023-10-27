from django.shortcuts import render
from .models import HelpContent, HomeCard, HomeCardExtra

# Create your views here.
def homePage(request):
    homeCard = HomeCard.objects.all()
    extraCard = HomeCardExtra.objects.all()
    
    parameters = {
        "cards" : homeCard,
        "extraCards" : extraCard
    }
    return render(request, "ContentPage/home.html", parameters)

def helpPage(request):
    helpContent = HelpContent.objects.all()
    
    parameters = {
        "contents" : helpContent,
    }
    return render(request, "ContentPage/help.html", parameters)