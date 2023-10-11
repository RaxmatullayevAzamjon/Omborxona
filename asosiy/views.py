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
        natija = Maxsulot.objects.filter(ombor__user=request.user)
        qidiruv = request.GET.get("qidiruv_sozi")
        if qidiruv:
            natija = natija.filter(nom__contains=qidiruv
                    ) | natija.filter(brend__contains=qidiruv
                    ) | natija.filter(olchov=qidiruv)

        content = {
            "products": natija
        }
        return render(request, "products.html",content)
    def post(self, request):
        Maxsulot.objects.create(
            nom = request.POST.get("n"),
            narx = request.POST.get("narx"),
            miqdor = request.POST.get("m"),
            brend = request.POST.get("b"),
            olchov = request.POST.get("o"),
            ombor = Ombor.objects.get(user=request.user)
        )
        return redirect("/products/")

def Product_edit(requests, son):
    if requests.method == "POST":
        Maxsulot.objects.filter(id=son).update(
            narx=requests.POST.get("n"),
            miqdor=requests.POST.get("m")
        )
        return redirect("/products/")
    content = {
        "maxsulot": Maxsulot.objects.get(id=son)
    }
    return render(requests, "product_update.html",content)

class MijozView(View):
    def get(self, request):
        natija = Mijoz.objects.filter(ombor__user=request.user)
        qidiruv = request.GET.get("qidiruv_sozi")
        if qidiruv:
            natija = natija.filter(ism__contains=qidiruv
                    ) | natija.filter(nom__contains=qidiruv
                    ) | natija.filter(manzil__contains=qidiruv)

        content = {
        "mijozlar": natija
        }
        return render(request, "clients.html",content)


def Mijoz_ochir(request, son):
    Mijoz.objects.filter(id=son).delete()
    return redirect("/mijoz/")

def Mijoz_edit(request, son):
    if request.method == "POST":
        Mijoz.objects.filter(id=son).update(
            ism=request.POST.get("i"),
            tel=request.POST.get("t"),
            qarz=request.POST.get("q")
        )
        return redirect("/mijoz/")
    content = {
        "mijoz": Mijoz.objects.get(id=son)
    }
    return render(request, "client_update.html",content)