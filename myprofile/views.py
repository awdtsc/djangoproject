from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render

def top(request):
    context = {
        'name':'たろう',
    }
    return render(request, 'myprofile/top.html',context)

def resume(request):
    return render(request, 'myprofile/resume.html')