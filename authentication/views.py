from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import PhoneNumberForm
from .models import PhoneNumber
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
    """
    ویو تایید کد امنیتی (OTP)
    """
    try:
        # دریافت رکورد شماره تلفن از دیتابیس
        phone_record = PhoneNumber.objects.get(phone_number=phone_number)
    except PhoneNumber.DoesNotExist:
        return HttpResponse("شماره تلفن معتبر نیست.")  # خطای شماره تلفن نامعتبر

    # کد امنیتی از دیتابیس
    otp_code = phone_record.otp_code

    if request.method == "POST" and 'submit_otp' in request.POST:
        entered_otp = request.POST.get('otp_code')  # دریافت کد واردشده توسط کاربر

        # بررسی تطابق کد
        if otp_code == entered_otp:
            phone_record.entered_otp = entered_otp
            phone_record.save()

            # تایید موفق و هدایت به صفحه خانه
            return redirect('home')  # تغییر به صفحه دلخواه شما
        else:
            return HttpResponse("کد امنیتی اشتباه است. لطفاً دوباره تلاش کنید.")

    # ارسال اطلاعات به قالب
    return render(request, 'authentication/verify_otp.html', {
        'phone_number': phone_number,
        'otp_code': otp_code,  # کد امنیتی برای نمایش در قالب
    })
