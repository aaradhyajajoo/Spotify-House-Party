from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def main(request):
    return HttpResponse("<h1>Hello, world. You're at the main page.</h1>")
