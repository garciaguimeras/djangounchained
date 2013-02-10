from django.shortcuts import render_to_response, redirect
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext

from forms import LoginForm

def basic_home(request):
    user = request.user

    user_name = "visitor"
    if user.is_authenticated():
        user_name = user.first_name + " " + user.last_name + " (" + user.username + ")"
        
    params = {"user_name": user_name}
    return render_to_response("basic/home.html", params, context_instance = RequestContext(request))
    
def basic_login(request):
    user = request.user
    next_page = "home"
    if next_page in request.GET:
        next_page = request.GET["next"]
    if next_page in request.POST:
        next_page = request.POST["next"]        
    if user.is_authenticated():
        return redirect(next_page)

    error_message = ""
    form = LoginForm()        
    
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username = request.POST["username"], password = request.POST["password"])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect(next_page)
                else:
                    error_message = "Your account has been disabled!"
            else:
                error_message = "Your username or password were incorrect"
        else:
            error_message = "Please, write your credentials"                
    
    params = {"error_message": error_message, "next": next_page, "form": form}
    return render_to_response("basic/login.html", params, context_instance = RequestContext(request))
    
def basic_logout(request):
    user = request.user
    
    if user.is_authenticated():
        logout(request)
        
    return redirect("home")
