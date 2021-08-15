from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .form import UserRegisterForm

from django.http.request import HttpRequest
from typing import NewType
Request = NewType('Request', HttpRequest)

# def home_view(request:Request, *args, **kwargs):
#     return render(request, template_name='home.html')

def register_view(request:Request, *args, **kwargs):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password1 = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')
            if password1 == password2:
                if User.objects.filter(username=username).exists():
                    messages.info(request, "User name existed!")
                    return redirect('register')
                elif User.objects.filter(email=email).exists():
                    messages.info(request, "Email existed!")
                    return redirect('register')
                else: 
                    user = User.objects.create_user(username=username, email=email, password=password1)
                    user.save()
                    messages.info(request, "Account created successfully!")
                    return redirect('register')
            else:
                messages.info(request, "password not match")
                return redirect('register')
    else:
        form = UserRegisterForm()

    context = {
        'form' : form,
    }
    return render(request, template_name='register.html', context=context)

# def login_view(request:Request, *args, **kwargs):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = auth.authenticate(username=username, password=password)
#         if user is not None:
#             auth.login(request, user)
#             return redirect('home')
#         else:
#             messages.info(request, 'Username or Password is invalid!')
#             return redirect('login')
#     return render(request, template_name='login.html')