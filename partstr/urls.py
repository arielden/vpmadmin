from django.urls import path
from . import views

app_name = 'partstr'

urlpatterns = [
    #partstr views
    path('', views.home, name='home'),
    path('pn_list/<int:user_id>/', views.pn_list, name='pn_list'),
]