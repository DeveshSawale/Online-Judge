from django.urls import path
from OJ import views 

urlpatterns = [
    path('', views.index , name = "home"),
]