from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render,HttpResponse
from django.utils import timezone
from django.contrib import messages
import filecmp, os

from django.contrib.auth.decorators import login_required

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

@login_required(login_url='members:login')
def submitProblem(request,problem_id):
    curr_user = request.user
    f = request.FILES.get('solution' , False)
    a = request.POST['typedsol']
    if(f):
        with open('/Devesh/solution.cpp','wb+') as dest:
            for chunk in f.chunks():
                dest.write(chunk)
            code = dest.read()
    elif(len(a) != 0):
        with open('/Devesh/solution.cpp','w+') as dest:
            dest.write(a)
            code = dest.read()
    else:
        problem = get_object_or_404(Problem, pk=problem_id)
        messages.info(request, "Please select a file or write code in textarea ")
        context = { 'problem':problem}
        return render(request,'OJ/problemDetails.html', context)
    
    problem = get_object_or_404(Problem, pk = problem_id)
    os.system('g++ /Devesh/solution.cpp ')

    with open('/Devesh/input.txt' , 'w+') as input:
        n = problem.testcases_set.count()
        input.write(str(n))
        input.write('\n')
        for testcase in problem.testcases_set.all():
            input.write(testcase.input)
            input.write('\n')
    
    os.system('a.exe < /Devesh/input.txt > \Devesh\out.txt')
        

    out2 = problem.output.path
    out1 = '\Devesh\out.txt'
    print(code)

    if(filecmp.cmp(out1,out2,shallow=False)):
        messages.success(request, 'Your solution was accepted..')
        verdict = 'Accepted'
    else:
        messages.info(request, 'Your solution was not accepted..')
        verdict = 'Wrong answer'

    solution = Solution()
    solution.user = curr_user
    solution.language = 'cpp'
    solution.problem = Problem.objects.get(pk=problem_id)
    solution.verdict = verdict
    solution.submitted_at = timezone.now()
    
    solution.submitted_code = 'code'
    solution.save()

    os.remove('/Devesh/solution.cpp')
    os.remove('/Devesh/input.txt')
    os.remove('/Devesh/out.txt')
    os.remove('a.exe')

    return HttpResponseRedirect(reverse('oj:leaderboard'))


@login_required(login_url='members:login')
def leaderboard(request):
    solutions = reversed(Solution.objects.all())
    return render(request, 'oj/leaderboard.html', {'solutions' : solutions})
