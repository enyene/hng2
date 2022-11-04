from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from .utils import operation
import json


@csrf_exempt
@require_POST
def calculate(request):
    headers = {
        "Access-Control-Allow-Origin": "*",

    }

    data = json.loads(request.body)
    operation_type = data.get('operation_type')
    x = data.get('x')
    y = data.get('y')
    
 
    result = operation(operation_type=operation_type, x=x, y=y)
    
    
    return JsonResponse({
        "slackname":'enyene',
        'result':result ,
        "operation_type": operation_type},
        status=200,headers=headers)