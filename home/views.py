from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
# Create your views here.
#Password for user 'vaibhav' is 123456@@@vaibhav
def index(request):
    if request.user.is_anonymous:
        return redirect("login")
    return render(request, 'index.html')

def loginUser(request):

    if request.user.is_authenticated:
        return redirect("/")

    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        print(username, password)
        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect("/")

        else:
            # No backend authenticated the credentials
            return render(request, 'login.html')

    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect("/login")

