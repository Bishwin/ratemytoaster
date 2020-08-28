from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse("hello")


def upload(request):
    return HttpResponse("uploader")


def new_toaster(request):
    return HttpResponse("new_toaster")


def my_toaster(request):
    return HttpResponse("my_toaster")