
from django.contrib import admin
from django.urls import path
from asosiy.views import *



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Login.as_view()),
    path('bolimlar/', bolimlar),
    path('Logout/', Logout.as_view()),
    path('products/', Products.as_view()),
    path('product_edit/<int:son>/', Product_edit),
    path('mijoz/', MijozView.as_view()),
    path('Mijoz_edit/<int:son>/', Mijoz_edit),
    path('Mijoz_ochir/<int:son>/', Mijoz_ochir),
]
