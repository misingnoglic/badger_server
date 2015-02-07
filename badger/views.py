from django.shortcuts import render,HttpResponse
import json
#test
# Create your views here.

def index(request):
    d = {"hello":"world"}
    return HttpResponse(json.dumps(d), content_type='application/json')
