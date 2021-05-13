from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


def login_view(request):  # Authentication
    """

    """
    if request.method == "POST":
        username = request.POST.get("login-username")
        password = request.POST.get("login-password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Bienvenido {}".format(user.username))
            return HttpResponseRedirect(reverse("catalogue:item_list"))
        else:
            messages.error(request, "Credenciales inválidas")
    return render(request, "users/login.html", {})


def logout_view(request):
    logout(request)
    messages.success(request, "Hasta pronto")
    return HttpResponseRedirect(reverse("catalogue:item_list"))
