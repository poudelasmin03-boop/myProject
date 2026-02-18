from django.contrib import admin
from django.urls import path
from .views import home,atm_views,deposite,open_account_views,transfer,check_balance,statements_viwes

urlpatterns = [
    path('',home,name='home'),
    path('transfer',transfer,name='transfer'),  
    path('atm',atm_views,name='atm'),
    path('deposite',deposite,name='deposite'),
    path('open',open_account_views,name='open'),
    path('chcek',check_balance,name='check'), 
    path('statements',statements_viwes,name="statements")
]
