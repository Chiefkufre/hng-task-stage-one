from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt


import os
import openai
import json

def user_detail(response, *args, **kwargs):
    
    
    try:

        #  if the request methd is "GET", then try this

        if response.method == 'GET':

            context = {    
                "slackUsername": "LordBees",
                'backend': True, 
                'age': 27,
                'bio':'I am a software Engineer with 2 years experience in web development and architecture design'
        }
            return JsonResponse(data=context, content_type='application/json', status=200)

        else:
            # raise an error
            return HttpResponse(
                {"Only Get method allowed"}, status=401
            )
    except:
        JsonResponse(data={'something when wrong, please retry in 2 minutes'})

    return JsonResponse(data=context,content_type='application/json')




@csrf_exempt
def perform_calculation(request, operation_type=None, output=None):

    operations = {"addition": "+", "subtraction": "-", "multiplication": "*",}

    if request.POST:
        data = request.POST
    elif request.GET:
        return HttpResponse({"Only POST requests allowed in this endpoint"})
    
    else:
        data = json.loads(request.body)
    

    first_value = data['y']
    second_value = data['x']

    ops = data["operation_type"]

    # pre-processing-convert to lower case-remove white spaces-

    operation = ops.lower().strip().replace(" ", "")

    # check if operation ia in operations dictionary

    if operation in operations:
        operation_type = operation
        output = eval(f"{first_value}{operations[operation_type]}{second_value}")
    
    else:
        operation_type = data['operation_type']
        output = "Invalid operation_type: {0}.Please enter a valid operational type-like adittion | multiplication | substraction".format(operation_type)

    context = {
        "slackUsername": "Chiefkufre",
        "result": output,
        "operation_type": operation_type
    }
    
    return JsonResponse(context)