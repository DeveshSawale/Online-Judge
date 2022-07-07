from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render,HttpResponse
from django.utils import timezone
from django.contrib import messages
import filecmp, os

from .models import Problem, Solution

# Create your views here.

def problems(request):
    problem_list = Problem.objects.all()
    context = { 'problem_list' : problem_list}
    return render(request, 'OJ/problems.html', context)

def problemDetails(request,problem_id):
    problem = get_object_or_404(Problem, pk=problem_id)
    context = { 'problem':problem}
    return render(request,'OJ/problemDetails.html', context)

def submitProblem(request,problem_id):
    f = request.FILES.get('solution' , False)
    a = request.POST['typedsol']
    if(f):
        with open('/Devesh/solution.cpp','wb+') as dest:
            for chunk in f.chunks():
                dest.write(chunk)
    elif(len(a) != 0):
        with open('/Devesh/solution.cpp','w') as dest:
            dest.write(a)
    else:
        problem = get_object_or_404(Problem, pk=problem_id)
        messages.info(request, "Please select a file or write code in textarea ")
        context = { 'problem':problem}
        return render(request,'OJ/problemDetails.html', context)
    
    os.system('g++ /Devesh/solution.cpp ')
    os.system('a.exe < /Devesh/input.txt > /Devesh/out.txt')
        

    out1 = '/Devesh/out.txt'
    out2 = '/Devesh/acc_out.txt'

    if(filecmp.cmp(out1,out2,shallow=False)):
        messages.success(request, 'Your solution was accepted..')
        verdict = 'Accepted'
    else:
        messages.info(request, 'Your solution was not accepted..')
        verdict = 'Wrong answer'

    solution = Solution()
    solution.language = 'cpp'
    solution.problem = Problem.objects.get(pk=problem_id)
    solution.verdict = verdict
    solution.submitted_at = timezone.now()
    solution.submitted_code = '/Devesh/solution.cpp'
    solution.save()

    return HttpResponseRedirect(reverse('oj:leaderboard'))


def leaderboard(request):
    solutions = Solution.objects.all()
    return render(request, 'oj/leaderboard.html', {'solutions' : solutions})
