from django.urls import path
from . import views

app_name = 'partstr'

urlpatterns = [
    #cg_calc views
    path('', views.partnumber_list, name='partnumbers_list'),
]