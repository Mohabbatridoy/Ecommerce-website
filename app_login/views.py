from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.urls import reverse

#Authentication
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate

# forms and models
from .models import Profile
from .forms import ProfileForm, SignUpForm


# Create your views here.
def sign_up(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
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
                return HttpResponse('Logged In')
    return render(request, 'app_login/login.html', context={'form':form})


@login_required
def log_out(request):
    logout(request)
    return HttpResponseRedirect(reverse('app_login:login'))