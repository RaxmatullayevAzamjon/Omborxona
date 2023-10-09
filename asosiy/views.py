from django.shortcuts import render,redirect
from django.contrib.auth import logout, authenticate,login
from django.views import View
from .models import *

class Login(View):
    def get(self,request):
        return render(request,"home.html")

    def post(self, request):
        user = authenticate(
            username = request.POST.get("login"),
            password = request.POST.get("parol")
        )
        if user is not None:
            login(request, user)
            return redirect("/bolimlar/")
        return redirect("/")

def bolimlar(request):
    return render(request,"bulimlar.html")

class Logout(View):
    def get(self, request):
        logout(request)
        return redirect("/")

class Products(View):
    def get(self, request):
        content = {
            "products": Maxsulot.objects.filter(ombor=request.user)
        }
        return render(request, "products.html",content)
    def post(self, request):
        Maxsulot.objects.create(
            nom = request.POST.get("n"),
            narx = request.POST.get("narx"),
            miqdor = request.POST.get("m"),
            brend = request.POST.get("b"),
            olchov = request.POST.get("o"),
            ombor = Ombor.objects.get(id=request.user.id)
        )
        return redirect("/products/")

class MijozView(View):
    def get(self, request):
        content = {
        "mijozlar": Mijoz.objects.filter(ombor=request.user)
        }
        return render(request, "clients.html",content)

def Mijoz_ochir(request, son):
    Mijoz.objects.filter(id=son).delete()
    return redirect("/mijoz/")
