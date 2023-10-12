from django.shortcuts import render,redirect
from django.contrib.auth import logout, authenticate,login
from django.views import View
from .models import *

def StatsView(request):
    content = {
        "stats": Statistika.objects.filter(ombor__user=request.user)
    }
    return render(request,"stats.html",content)





