from django.urls import path
from . import views

app_name = 'partstr'

urlpatterns = [
    #partstr views
    path('', views.home, name='home'), # 'partstr/' home.
    path('partlist/<int:user_id>/', views.partlist, name='partlist'),
    path('partcreate/', views.partcreate, name='partcreate'),
    path('partupdate/<int:pk>/', views.partupdate, name='partupdate'),
]