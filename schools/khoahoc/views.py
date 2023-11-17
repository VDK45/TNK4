from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Home")


def course(request):
    return HttpResponse("Khoa hoc.")


def cabinet(request):
    return HttpResponse("Lop hoc.")
