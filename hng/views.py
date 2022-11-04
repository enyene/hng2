from rest_framework.decorators import api_view
from django.views.decorators.http import require_GET
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from django.http import JsonResponse
from .utils import operation
import json


@require_GET
def api(request):
    data = {
        "slackUsername":'iEnyene',
        "backend":True,
        "age":23,
        "bio":'am a backend developer'  
        }
    response = JsonResponse(data)
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "GET, OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type"
    return response


@csrf_exempt
@api_view(['POST'])
def calculate(request):
    headers = {
        "Access-Control-Allow-Origin": "*",

    }

    data = json.loads(request.body)
    operation_type = data.get('operation_type')
    x = data.get('x')
    y = data.get('y')
    
 
    result = operation(operation_type=operation_type, x=x, y=y)
    
    
    return Response({
        "slackname":'enyene',
        'result':result ,
        "operation_type": operation_type},
        status=200,headers=headers)