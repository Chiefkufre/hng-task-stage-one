from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt


import os
import openai
import json

from .utilis import openai_response

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



openai.api_key = os.environ.get("OPENAI_APP_KEY ")

@csrf_exempt
def perform_calculation(request:HttpRequest, operation_type=None, output=None):

    operations = {"addition": "+", "subtraction": "-", "multiplication": "*",}
    
    if request.POST:
        data = request.POST
    elif request.GET:
        return JsonResponse(data={"Only POST requests allowed in this endpoint"})
    
    elif request.body:

        data = json.loads(request.body)
    
        # convert json input to integers
        first_value = int(data['y'])
        second_value = int(data['x'])

        ops = data["operation_type"]

        # pre-processing-convert to lower case-remove white spaces-

        operation = ops.lower().strip().replace(" ", "")

        # check if operation is in operations dictionary

        if operation in operations:
            operation_type = operation

            # convert out put to integer
            output = int(eval(f"{first_value}{operations[operation_type]}{second_value}"))
            context = {
                 "slackUsername": "Chiefkufre",
                "result": output,
                "operation_type": operation_type
            }
               
            return JsonResponse(context)
    
    else:
        data = json.loads(request.body)
        query = str(data['prompt'])

        response = openai.Completion.create(
            model = "text-davinci-002",
            prompt = query,
            temperature=0,
            max_tokens=130,
            frequency_penalty=0,
            presence_penalty=0

        )
        if "choices" in response:
            alternative_terms = {"sum":"addition", "multiplication":"product", "differnce":"subtraction"}
            output = response['choices'][0]['text']
            for ops in alternative_terms:
                operation_type = None
                new_query = set(query.split())
                if ops in new_query:
                    operation_type = ops.lower()
            return JsonResponse({
                "slackUsername": "Chiefkufre",
                "result": output,
                "operation_type": operation_type
            })
        # operation_type = data['operation_type']
        # output = "Invalid operation_type: {0}.Please enter a valid operational type-like adittion | multiplication | substraction".format(operation_type)

    