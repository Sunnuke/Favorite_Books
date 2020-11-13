from django.shortcuts import render, redirect, HttpResponse

# Create your views here.

def books(request):
    return HttpResponse('Hi Human!!!')