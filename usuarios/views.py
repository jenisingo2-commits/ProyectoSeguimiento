from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Empleado
from django.shortcuts import render

def home(request):
    return render(request, "home.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Usuario o contraseña incorrectos")

    return render(request, "login.html")


def registro(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if password1 != password2:
            messages.error(request, "Las contraseñas no coinciden")
            return redirect("registro")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Ese usuario ya existe")
            return redirect("registro")

        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()

        messages.success(request, "Usuario registrado correctamente. Ahora inicia sesión.")
        return redirect("login")

    return render(request, "registro.html")


def logout_view(request):
    logout(request)
    return redirect("login")

@login_required
def dashboard(request):
    total_empleados = Empleado.objects.count()
    return render(request, 'dashboard.html', {
        'total_empleados': total_empleados
    })
    return render(request, 'usuarios/base.html') 
