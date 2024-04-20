from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserRegistrationsForm, ProfileForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                messages.success(request, 'Login successful')
                return redirect('book:home')
            else:
                messages.error(request, 'Disabled account')
        else:
                messages.warning(request, 'invalid login')

    return render(request, 'account/login.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationsForm(request.POST)
        if form.is_valid():
            new = form.save(commit=False)
            new.save()
            messages.success(request, 'Account Created Successfully, login to continue')
            return redirect('login')
        else:
            if 'password2' in form.errors:
                messages.error(request, 'Passwords do not match.')
            elif 'username' in form.errors:
                messages.error(request, 'A user with that username already exists.')
            elif 'email' in form.errors:
                messages.error(request, 'A user with that email address already exists.')
            else:
                messages.error(request, 'There was an error with your signup. Please try again.')
            return redirect('signup')
    else:
        form = UserRegistrationsForm()
    return render(request, 'account/signup.html', {'form': form})

def user_logout(request):
    logout(request)
    messages.success(request, 'User logged out successfully')
    return redirect('login')

def profile_view(request, username=None):
    if username:
        profile = get_object_or_404(User, username=username).profile
    else:
        profile = request.user.profile
    return render(request, 'account/profile.html', {'profile' : profile})

def profile_edit(request):
    form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
    if form.is_valid():
        form.save()
        messages.success(request, "Profile updated successfuly")
        return redirect('profile')
    else:
        messages.error(request, "Please correct the error below.")
    return render(request, 'account/edit_profile.html', {'form': form})

def profile_delete(request):
    user = request.user

    if request.method == 'POST':
        logout(request)
        user.delete()
        messages.warning(request, "Your account has been deleted!")

    return render(request, 'account/profile.html', {'user': user})
