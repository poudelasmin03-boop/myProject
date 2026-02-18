
from django.urls import path
from app.views import home_views,form_views,flush_data

urlpatterns = [
    path('',home_views,name="home"),
    path('form',form_views,name="form"),
    path('data',flush_data,name='data')
    
]
