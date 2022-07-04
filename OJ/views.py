from django.shortcuts import render,HttpResponse

from .models import Problem, Solution

# Create your views here.

def problems(request):
    return HttpResponse("Problems Page")

def problemDetails(request):
    return HttpResponse("problemDetails Page")

def submitProblem(request):
    return HttpResponse("Submit Problem Page")

def leaderboard(request):
    return HttpResponse("Leaderboard Page")
