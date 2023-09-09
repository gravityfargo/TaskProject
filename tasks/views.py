from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Suh Dude")

def detail(self, task_id):
    response = "deets %s"
    return HttpResponse(response & task_id)