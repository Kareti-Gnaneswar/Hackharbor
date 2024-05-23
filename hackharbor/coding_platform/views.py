from django.shortcuts import render, redirect
from .models import User

def home(request):
    return render(request, 'coding_platform/home.html')

def career(request):
    return render(request, 'coding_platform/career.html')

def Learning(request):
    return render(request, 'coding_platform/Learning.html')

def contest(request):
    return render(request, 'coding_platform/contest.html')

def hiring(request):
    return render(request, 'coding_platform/hiring.html')

def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username, password=password)
            # Perform login logic here
            return redirect('home')  # Redirect to home page after successful login
        except User.DoesNotExist:
            return render(request, 'coding_platform/Login.html', {'error': 'Invalid credentials.'})
    else:
        return render(request, 'coding_platform/Login.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        user = User.objects.create(username=username, password=password, email=email)
        # Perform signup logic here
        return redirect('Login')  # Redirect to login page after successful signup
    else:
        return render(request, 'coding_platform/signup.html')
