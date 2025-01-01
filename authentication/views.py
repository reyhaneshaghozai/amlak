from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from .forms import PhoneNumberForm , SignupForm
from .models import PhoneNumber,Signup
import random

def login(request):
    form = PhoneNumberForm()
    if request.method == "POST":
        form = PhoneNumberForm(request.POST)
        if form.is_valid():
            form.save()
            # هدایت به صفحه تایید کد
            return redirect('home:home')    


    return render(request, 'authentication/login.html', {'form': form})

def register(request):
    form = SignupForm()
    error = None
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if cd['password1'] == cd['password2']:
                if not User.objects.filter(username=cd['phone_number']).exists():
                    user = User.objects.create_user(
                        username=cd['phone_number'],
                        email=cd['email'],
                        password=cd['password1'],
                    )
                    user.save()
                    return redirect('home:home')
                else:
                    form.add_error('phone_number', "شماره تلفن قبلاً ثبت شده است.")
            else:
                    form.add_error('password2', 'رمز عبور و تکرار آن یکسان نیستند.')

    return render(request, 'authentication/register.html', {'form': form, 'error': error})
