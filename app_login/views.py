from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.urls import reverse

#Authentication
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate

# forms and models
from .models import Profile
from .forms import ProfileForm, SignUpForm

#to show messages
from django.contrib import messages


# Create your views here.
def sign_up(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully!")
            return HttpResponseRedirect(reverse('app_login:login'))
    return render(request, 'app_login/signup.html', context={'form':form,})


def log_in(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('app_shop:home'))
    return render(request, 'app_login/login.html', context={'form':form})


@login_required
def log_out(request):
    logout(request)
    messages.warning(request, "You are Logged out!")
    return HttpResponseRedirect(reverse('app_shop:home'))



@login_required
def user_profile(request):
    profile = Profile.objects.get(user=request.user)
    form = ProfileForm(instance=profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.info(request, "Profile saved!")
            form = ProfileForm(instance=profile)

    return render(request, 'app_login/edit_profile.html', context={'form':form})