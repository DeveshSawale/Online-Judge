from django.contrib import admin
from .models import Problem, TestCases,Solution

# Register your models here.
admin.site.register(Problem)
admin.site.register(TestCases)
admin.site.register(Solution)
