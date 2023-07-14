from django.shortcuts import render, redirect, HttpResponse
from app_user.forms import NewUserForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def user_signup(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()                                 # user entry in auth_user table
            print(user)
            messages.success(request, "Registration successful.")
            return redirect('user_login') 
    
    elif request.method == "GET":
        form = NewUserForm()
        return render(request= request, template_name= "user_register.html", context= {"signup_form": form})
    

def user_login(request):
    if request.method == "POST":
        # form = AuthenticationForm(request, data=request.POST)
        # if form.is_valid():
        #     user_name = form.cleaned_data.get("username")
        #     password = form.cleaned_data.get("password") 
        #     print(user_name, password)
        user_name = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=user_name, password=password)
        if user:
            login(request, user)   
            messages.success(request, "Logged in succesfully.")
            return redirect("home_page")
        else:
            messages.error(request, "Invalid username or password.")

    elif request.method == "GET":
        return render(request, "login.html", {"login_form": AuthenticationForm()})
    


def user_logout(request):
    logout(request)
    return redirect("user_login")
