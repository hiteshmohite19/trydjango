from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def auth_login(request):
    if request.method == "POST":
        request_body = request.POST
        content = {"status": False, "message": "Login failed"}
        user = authenticate(
            request,
            username=request_body.get("username"),
            password=request_body.get("password"),
        )
        if not user:
            return render(request, "auth/login.html", content)

        login(request, user)
        return redirect("/admin")
    content = {"status": True, "message": "Login failed"}
    return render(request, "auth/login.html", content)


def auth_logout(request):
    # if request.method == "POST":
    logout(request)
    return redirect("/")
    # return render(request, "auth/login.html", {})
