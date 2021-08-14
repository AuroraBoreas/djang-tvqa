from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.
def home_view(request, *args, **kwargs):
    # print(args, kwargs)
    return render(request, template_name='index1.html', context={})

def register_view(request, *args, **kwargs):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password1']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Name is used!")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Name is used!")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email,password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, "Password Not Correct!")
    else:
        return render(request, template_name='register.html', context={})

def login_view(request, *args, **kwargs):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password1']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('react')
        else:
            messages.info(request, 'User Name or Password is invalid!')
            return redirect('login')
    return render(request, 'login.html')