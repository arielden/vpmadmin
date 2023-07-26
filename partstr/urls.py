from django.urls import path
from . import views

app_name = 'partstr'

urlpatterns = [
    #partstr views
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),

    path('', views.home, name='home'), # 'partstr/' home.
    path('partlist/', views.partlist, name='partlist'),
    path('partcreate/', views.partcreate, name='partcreate'),
    path('partupdate/<int:pk>/', views.partupdate, name='partupdate'),
    path('partdelete/<int:pk>/', views.partdelete, name='partdelete'),
    path('structure/', views.structure, name='structure'),
    path('catiaload/<int:pk>', views.catiaload, name='catiaload'),
    path('partloader/<int:pk>', views.partloader, name='partloader'),
]