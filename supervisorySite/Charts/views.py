from django.shortcuts import render, HttpResponse
from ClientOPC.OPCClientUA import OPCClientUA
from asyncua import ua
from asyncio import TimeoutError
import json
from Settings.getEndPoint import getEndPoint

# Create your views here.
async def lineChartJson(request) :
    def transformStrInListofTuple(data : str) -> list[tuple]:
        data = data.replace(' ', '')
        data = data.split("\n")
        return  [eval(file) for file in data[0:len(data) - 1]]
    
    try:
        endPoint = await getEndPoint()
        
        client = OPCClientUA(endPoint) if endPoint else OPCClientUA()
        await client.connect()
        temperature = await client.getHistoryDataFrom('temperature')    
        setPoint = await client.getHistoryDataFrom('setPoint')    
        await client.disconnect()
    except (ConnectionError, ua.UaError, TimeoutError):
        response = HttpResponse()
        response.status_code = 500
        return response

    temperature = transformStrInListofTuple(temperature)
    setPoint = transformStrInListofTuple(setPoint)

    labels = [str(data[2]) for data in temperature]
    temperature = [data[1] for data in temperature]
    setPoint = [data[1] for data in setPoint]

    if(len(labels) > 100):
        labels = labels[-100:]
        temperature = temperature[-100:]
        setPoint = setPoint[-100:]

    response = json.dumps({
        'type' : 'line',
        'data' : {
            'labels' : labels,
            'datasets' : [{
                'label' : 'temperature',
                'data' : temperature,
                'fill' : False,
                "backgroundColor": "rgba(232, 5, 5, 0.2)",
                "borderColor": "rgb(232, 5, 5)",
                "borderWidth": 1,
            },{
               'label' : 'setPoint',
                'data' : setPoint,
                'fill' : False,
                "backgroundColor": "rgba(113, 9, 145, 0.2)",
                "borderColor": "rgb(113, 9, 145)",
                "borderWidth": 1,
            }]
        },
        'options': {
            'responsive': True,
            'maintainAspectRatio': False,
            'animation': False,
        }
    })

    return HttpResponse(response)

def ChartFullPage(request):
    return render(request, "Charts/fullPageChart.html")