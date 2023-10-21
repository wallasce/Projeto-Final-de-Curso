from django.shortcuts import render

# Create your views here.
def homePage(request):
    return render(request, "ContentPage/home.html")

def helpPage(request):
    return render(request, "ContentPage/help.html")