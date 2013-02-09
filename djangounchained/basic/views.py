from django.shortcuts import render_to_response, redirect
from django.contrib.auth import authenticate, login, logout

def basic_home(request):
    user = request.user

    user_name = "visitor"
    if user.is_authenticated():
        user_name = user.first_name + " " + user.last_name + " (" + user.username + ")"
        
    params = {"user_name": user_name}
    return render_to_response("basic/hello.html", params)
    
def basic_login(request):
    user = request.user
    
    if user.is_authenticated():
        return redirect("home")
        
    error_message = ""
    user = authenticate(username="root", password="root")
    if user is not None:
        if user.is_active:
            login(request, user)
            return redirect("home")
        else:
            error_message = "Your account has been disabled!"
    else:
        error_message = "Your username and password were incorrect."
    
    params = {"error_message": error_message}
    return render_to_response("basic/login.html", params)
    
def basic_logout(request):
    user = request.user
    
    if user.is_authenticated():
        logout(request)
        
    return redirect("home")
