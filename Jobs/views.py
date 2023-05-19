from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from Jobs.forms import EmployerForm, SeekerForm


# Create your views here.
def index(request):
    return render(request,"Home/Modified_files/main.html")

@login_required
def admin_dashboard(request):
    return render(request, "Admin/Admin_dash.html")

@login_required
def seeker_dashboard(request):
    return render(request,"JobSeeker/USER_DASH.html")

@login_required
def employer_dashboard(request):
    return render(request,"Employer/EMPLOYER_DASH.html")


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Logged in as {user.username}")
            if user.is_staff:
                return redirect('admin_dashboard')
            elif user.is_recruiter:
                return redirect('employer_dashboard')
            elif user.is_seeker:
                return redirect('seeker_dashboard')
        else:
            messages.info(request, 'Invalid Credentials')
    return render(request,"Home/Modified_files/login.html")


def registration(request):
    if request.method == 'POST':
        employer_form = EmployerForm(request.POST)
        if employer_form.is_valid():
            user = employer_form.save(commit=False)
            user.password = make_password(employer_form.cleaned_data.get('password1'))
            user.is_recruiter = True
            user.save()
            return redirect('user_login')
    else:
        employer_form = EmployerForm()
    return render(request, 'Employer/reg.html', {'employer_form': employer_form})

def employee_registration(request):
    if request.method == 'POST':
        seeker_form = SeekerForm(request.POST)
        if seeker_form.is_valid():
            user = seeker_form.save(commit=False)
            user.password = make_password(seeker_form.cleaned_data.get('password1'))
            user.is_seeker = True
            user.save()
            return redirect('user_login')
    else:
        seeker_form = SeekerForm()
    return render(request, 'JobSeeker/reg_seeker.html', {'seeker_form': seeker_form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('user_login')