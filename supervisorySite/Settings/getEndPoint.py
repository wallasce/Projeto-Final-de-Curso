from asgiref.sync import sync_to_async
from .models import EndPoint

@sync_to_async
def getEndPoint():
    if(EndPoint.objects.count() == 1):
        endPoint = EndPoint.objects.first()
        return endPoint.ipAddress + ":" + endPoint.port
    else:
        return False
