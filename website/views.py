from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.
def home(request):

    #check to see if logged in
    if request.method == "POST":
        username = request.POST['Username']
        password = request.POST['Password']

        #Authenticate
        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request,user)
            messages.success(request,"You Have Been Logged In")
            return redirect('home')
        
        else: 
            messages.success(request, "There was an error loggin in. Please Try again!")
            
    else:
        pass

    return render(request, 'home.html', {})


# def login_user(request):
#     pass

def logout_user(request):
    logout(request)
    messages.success(request, "You Have Been Logged Out...")
    return redirect('home')

def register_user(request):

    return render(request, 'register.html', {})
