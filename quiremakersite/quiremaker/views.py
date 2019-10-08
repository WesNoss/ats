from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import Context, loader
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def index(request):
    template = loader.get_template("quiremaker/index.html")
    return HttpResponse(template.render())

@csrf_exempt
def submitted(request):
    dict = request.POST
    template = loader.get_template("quiremaker/submitted.html")
    return HttpResponse(template.render())