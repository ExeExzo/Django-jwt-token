from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from .serializers import UserSerializer
from rest_framework import viewsets
from .models import *

# Create your views here.

def loginPage(request):
    if request.user.is_authenticated: 
        return redirect('main')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username = username, password = password)

            if user is not None:
                login(request, user)
                return redirect('main')
            else:
                messages.info(request, 'Неправильный пароль или логин')

        context = {

        }
        return render(request, 'main/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def main(request):
    users = User.objects.all() 
    context = { 
        "users":users,
    }
    return render(request,'main/main.html', context=context)

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all() # quersyset ozgertu kerek
    permission_classes = (IsAdminUser,)