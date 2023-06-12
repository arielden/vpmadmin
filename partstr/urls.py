from django.urls import path
from . import views

app_name = 'partstr'

urlpatterns = [
    #partstr views
    path('', views.home, name='home'),
    path('pn_list/<str:id>/', views.pn_list, name='pn_list'),
]