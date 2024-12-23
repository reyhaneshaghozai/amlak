from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from .forms import PhoneNumberForm , SignupForm
from .models import PhoneNumber,Signup
import random

def collect_phone_number(request):
    if request.method == "POST" and 'submit_phone' in request.POST:
        form = PhoneNumberForm(request.POST)

        if form.is_valid():
            phone_number = form.cleaned_data['phone_number']

            phone_record, created = PhoneNumber.objects.get_or_create(phone_number=phone_number)

            otp_code = str(random.randint(100000, 999999))
            phone_record.otp_code = otp_code
            phone_record.entered_otp = "" 
            phone_record.save()

            # هدایت به صفحه تایید کد
            return redirect('authentication:verify_otp', phone_number=phone_number)  
    else:
        form = PhoneNumberForm()

    return render(request, 'authentication/authentication.html', {'form': form})


def verify_otp(request, phone_number):
    try:
        phone_record = PhoneNumber.objects.get(phone_number=phone_number)
    except PhoneNumber.DoesNotExist:
        return HttpResponse("شماره تلفن معتبر نیست.") 

    otp_code = phone_record.otp_code

    if request.method == "POST" and 'submit_otp' in request.POST:
        entered_otp = request.POST.get('otp_code') 

        if otp_code == entered_otp:
            phone_record.entered_otp = entered_otp
            phone_record.save()

            return redirect('home') 
        else:
            return HttpResponse("کد امنیتی اشتباه است. لطفاً دوباره تلاش کنید.")

    return render(request, 'authentication/verify_otp.html', {
        'phone_number': phone_number,
        'otp_code': otp_code, 
    })

def signup(request):
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
                    return redirect('home')
                else:
                    error = "شماره تلفن قبلاً ثبت شده است."
            else:
                error = "رمز عبور و تکرار آن یکسان نیستند."
    return render(request, 'authentication/signup.html', {'form': form, 'error': error})
