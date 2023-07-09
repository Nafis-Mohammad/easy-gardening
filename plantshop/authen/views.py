from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.urls import reverse
from plantapp.models import Customer





def signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        # Password checking
        if password != password2:
            messages.error(request, "Passwords do not match. Please try again!")
            return redirect(reverse('authen:signup'))

        try:
            if User.objects.get(username=email):
                messages.warning(request, "Email already exists.")
                return redirect(reverse('authen:signup'))
        except User.DoesNotExist:
            pass

        # Check for error inputs
        user = User.objects.create_user(email, email, password)
        Customer.objects.create(user=user, name=user.username, email=user.email)
        user.save()
        messages.info(request, 'Thanks for signing up!')
        
        return redirect(reverse('authen:handlelogin'))

    return render(request, 'auths/signup.html')


def handlelogin(request):
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            # messages.success(request, "Login Success")
            return render(request, 'index.html')
        else:
            messages.error(request, "Invalid credentials")
            return redirect('/authen/login/')

    return render(request, 'auths/login.html')

def handlelogout(request):
    logout(request)
    messages.success(request,"Logout Success")
    return redirect('/authen/login/')
