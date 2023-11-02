from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import AppUser
from django.core.mail import send_mail
from django.utils.crypto import get_random_string
# Create your views here.


@login_required(login_url='login/')
def profile(request):
    template = 'user/profile.html'
    
    context = {}
    return render(request, template, context)


def login(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            remember_me = request.POST.get('remember_me')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                if remember_me:
                    request.session.set_expiry(60 * 60 * 24 * 14)   # Set a longer session timeout (e.g., 2 weeks)
                else:
                    request.session.set_expiry(0)    
                next_url = request.GET.get('next')
                if next_url:
                    return redirect(next_url)
                else:
                    return redirect('dashboard')
            else:
                messages.info(request, 'Invalid password or username')
                return redirect(request.get_full_path()) # Need to return current URL cause next URL and normal URL are different
        else:
            template = 'user/login.html'
            return render(request, template)
    




def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        if password1 and password1 == password2:
            if AppUser.objects.filter(username=username).exists():
                messages.info(request,'This username has already taken')
                return redirect('register')
            elif AppUser.objects.filter(email=email):
                messages.info(request,"This email has already taken")
                return redirect('register')
                
            else:
                user = AppUser.objects.create_user(username=username, password=password1, first_name=first_name, last_name=last_name, email=email)
                user.save()
                
                
                activation_code = get_random_string(30)
                user.activation_code = activation_code
                user.save()

                # Send activation email
                # activation_link = f'http://127.0.0.1:8000/activate/{activation_code}/'
                # send_mail(
                #     'Activate Your Account',
                #     f'Click the following link to activate your account: {activation_link}',
                #     'from@example.com',
                #     [email],
                #     fail_silently=False,
                # )
                
                messages.info(request, 'Successfully created account')
                return redirect('login')
        else:
            messages.info(request, "Password dosen't match")
            return redirect('register')
    else:
        template = 'user/register.html'
        return render(request, template)
    
    
    
def activate_account(request, activation_code):
    try:
        user = AppUser.objects.get(activation_code=activation_code, is_active=False)
    except AppUser.DoesNotExist:
        # Handle the case where the activation code is invalid or the account is already active
        return render(request, 'user/activation_failed.html')

    # Activate the user account
    user.activate()
    return render(request, 'user/activation_success.html')
    
    
    
    
    
    
    
    


def forget(request):
    template = 'user/forget.html'
    
    context = {}
    return render(request, template, context)


def logout(request):
    auth.logout(request)
    return redirect('/')