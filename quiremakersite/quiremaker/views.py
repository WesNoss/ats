from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import Context, loader

def index(request):
    template = loader.get_template("quiremaker/index.html")
    return HttpResponse(template.render())

def submitted(request):
    template = loader.get_template("quiremaker/submitted.html")
    return HttpResponse(template.render())