from django.shortcuts import render, redirect
from django.views import View
from .forms import UserCreateForm, LoginForm, ProfileForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .models import User
from django.contrib.auth.mixins import LoginRequiredMixin


class Register(View):
    def get(self, request):
        return render(request, 'register.html')
    
    def post(self, request):
        if request.method == 'POST':
            username = request.POST.get('username')
            first =request.POST.get('first')
            last = request.POST.get('last')
            email =request.POST.get('email')
            password = request.POST.get('password')
            User.objects.create_user(username=username, first_name=first, last_name=last, email=email, password=password)
            return redirect('login')
        return render(request, 'register.html')
    
    

class Login (View):
    def get(self, request):
        return render(request, 'login.html')
    
    
    def post(self, request):
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            return render(request, 'login.html')
        return render(request, 'login.html')
    
    
class Logaut(View, LoginRequiredMixin):
    def get(self, request):
        logout(request)
        return redirect('users:login')
    
class Profile(View, LoginRequiredMixin):
    def get(self, request):
        print('salom')
        user = User.objects.get(id=request.user.id)
        print(user)
        context = {'user': user}
        return render(request, 'profile.html', context=context) 
    
    
class Prifile_edit(View, LoginRequiredMixin):
    def get(self, request):
        user = request.user
        context = {'user': user}
        return render(request, 'profile_edit.html', context)
    
    def post(self, request):
        user = request.user
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        user.username = username
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.save()
        return redirect('users:profile')
     