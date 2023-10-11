from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Ombor(models.Model):
    # id, usename, password, is_staff, is_superuser, is_active
    nom = models.CharField(max_length=30)
    manzil = models.CharField(max_length=150)
    ism = models.CharField(max_length=50)
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.nom


d = (
    ("Kg","Kg"),
    ("dona","dona"),
    ("litr","litr")
)
class Maxsulot(models.Model):
    nom = models.CharField(max_length=30)
    narx = models.PositiveSmallIntegerField()
    miqdor = models.PositiveSmallIntegerField()
    olchov = models.CharField(max_length=30,choices=d)
    ombor = models.ForeignKey(Ombor,on_delete=models.CASCADE)
    brend = models.CharField(max_length=20,null=True,blank=True)

    def __str__(self):
        return self.nom

class Mijoz(models.Model):
    nom = models.CharField(max_length=30)
    manzil = models.CharField(max_length=30)
    ism = models.CharField(max_length=30)
    tel = models.CharField(max_length=20)
    ombor = models.ForeignKey(Ombor,on_delete=models.CASCADE)
    qarz = models.CharField(max_length=50,null=True,blank=True)

    def __str__(self):
        return self.nom

