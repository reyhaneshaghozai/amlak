from django.shortcuts import render
from django.http import HttpResponse
from .forms import PhoneNumberForm
from .models import PhoneNumber

def collect_phone_number(request):
    if request.method == "POST":
        form = PhoneNumberForm(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data['phone_number']
            if not PhoneNumber.objects.filter(phone_number=phone_number).exists():
                PhoneNumber.objects.create(phone_number=phone_number)
                return HttpResponse(f"شماره تلفن {phone_number} با موفقیت ذخیره شد.")
            else:
                return HttpResponse(f"شماره تلفن {phone_number} قبلاً ذخیره شده است.")
    else:
        form = PhoneNumberForm()

    return render(request, 'authentication/authentication.html', {'form': form})
