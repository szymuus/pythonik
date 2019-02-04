from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse("heeelo")
# Create your views here.
