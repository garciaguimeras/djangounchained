from django.shortcuts import render_to_response

def home(request):
    params = {}
    return render_to_response("basic/hello.html", params)
    
def login(request):
    params = {}
    return render_to_response("basic/login.html", params)
