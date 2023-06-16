from django.urls import path
from . import views

app_name = 'partstr'

urlpatterns = [
    #partstr views
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),

    path('', views.home, name='home'), # 'partstr/' home.
    path('partlist/<int:user_id>/', views.partlist, name='partlist'),
    path('partcreate/', views.partcreate, name='partcreate'),
    path('partupdate/<int:pk>/', views.partupdate, name='partupdate'),
    path('partdelete/<int:pk>', views.partdelete, name='partdelete'),
]