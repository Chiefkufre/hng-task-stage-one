from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

from rest_framework.response import Response
from rest_framework import generics

from .models import HngUserModel
from .userSerializer import HngUserSerializer

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



class User_views(generics.ListCreateAPIView):

    queryset = HngUserModel.objects.all()
    serializer_class = HngUserSerializer