from django.db import models
from asosiy.models import *


class Statistika(models.Model):
    maxsulot = models.ForeignKey(Maxsulot,on_delete=models.CASCADE)
    mijoz = models.ForeignKey(Mijoz,on_delete=models.CASCADE)
    ombor = models.ForeignKey(Ombor,on_delete=models.CASCADE)
    sana = models.DateField()
    miqdor = models.PositiveIntegerField()
    summa = models.PositiveIntegerField()
    tolangan_summa = models.PositiveIntegerField()
    nasiya = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.maxsulot.nom

