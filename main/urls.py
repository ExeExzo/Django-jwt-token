from django.urls import path,include
from django.contrib import admin 
from .import views
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'users',views.UserViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('login/', views.loginPage, name='login'), 
    path('logout/', views.logoutUser, name='logout'),
    path ('main/',  views.main, name='main'),
    
]
