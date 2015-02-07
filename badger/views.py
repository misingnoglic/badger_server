from django.shortcuts import render,HttpResponse
import json
from django.core import serializers
from models import Location, Badge
# Create your views here.

def index(request):
    d = {"hello":"world"}
    return HttpResponse(json.dumps(d), content_type='application/json')

def locations(request):
    data = serializers.serialize('json', Location.objects.all())
    return HttpResponse(data, content_type='application/json')

def badges(request):
    data = serializers.serialize('json', Badge.objects.all())
    return HttpResponse(data, content_type='application/json')

def scantron(request,name):
    name = str(name.upper())
    matrix =[[" " for x in range(len(name)+1)] for x in range(26+1)]
    letters = [chr(i) for i in range(65,90+1)]
    print letters
    for i in range(len(name)):
        if not (name[i])==" ":
            j = letters.index(name[i])
            matrix[j][i+1]="X"

    for i in range(len(matrix)-1):
        matrix[i][0] = letters[i]

    matrix = [[" "]+list(range(1,len(matrix[0])))]+matrix
    return HttpResponse(str(matrix))