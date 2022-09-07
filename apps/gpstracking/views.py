from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def maptracking(request):

    return render(request,"gpstracking/maptracking.html",)
    # return render(request,"gpstracking/a1.html",)
