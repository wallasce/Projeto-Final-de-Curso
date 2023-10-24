from django.shortcuts import render, redirect

from .form import EndPointForm
from .models import EndPoint

# Create your views here.
def deleteOldEndpoint(oldEndPoints) -> None:
    for endPoint in oldEndPoints:
        endPoint.delete()

def ChangeEndPoint(request):
    form = EndPointForm(request.POST or None)

    if (request.method == 'POST'):
        if (form.is_valid()):
            oldEndPoints = EndPoint.objects.all()
            deleteOldEndpoint(oldEndPoints)
            
            form.save()
            return redirect("/hmi")
    else:
        parameters = {
            "form" : form,
            "endPoint" : EndPoint.objects.all()
        }
    return render(request, "Settings/settingEndPoint.html", parameters)