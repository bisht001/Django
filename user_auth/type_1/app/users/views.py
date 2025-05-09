from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        email = request.POST["email"]
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]

        if User.objects.filter(username=username).exists():
            messages.error("Usename already taken")
        
        else:
            new_user = User.objects.create_user(username=username,
                                            email=email, 
                                            password=password,
                                            first_name=first_name,
                                            last_name=last_name
                                            )
            new_user.save()

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home_page")
            
            else:
                messages.error("Their is some error please try after some time.")

    else:
        return render(request,'users/signup.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home_page")
            
        else:
            messages.error("Their is some error please try after some time.")

    else:

        # gives you the URL of the page that redirected on the current page
        reference = request.META.get("HTTP_REFERER")
        if reference is None:
            return render(request,'signup_page')
        else:
            return render(request,'users/login.html') 


@login_required(login_url="signup_page")
def logout_view(request):
    logout(request)
    return redirect('home_page')
