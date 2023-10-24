from django.shortcuts import render

# Create your views here.
def errorPage(request):
    return render(request, "webSiteConfig/serverError.html")