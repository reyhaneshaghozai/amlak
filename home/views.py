from django.shortcuts import render,redirect
from .forms import PropertyRequestForm ,RentalPropertyForm,RentalPropertyRequestForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

def home(request):
    return render(request, 'home/home.html')

@login_required(login_url='/signup/')
def buy_property(request):
    if request.method == 'POST':
        form = PropertyRequestForm(request.POST)
        if form.is_valid():
            property_request = form.save()
            messages.success(request, "درخواست شما با موفقیت ثبت شد!")
            return redirect('home')
        else:
            print(form.errors)  
            messages.error(request, "لطفاً اطلاعات وارد شده را بررسی کنید.")
    else:
        form = PropertyRequestForm()
    return render(request,'home/buy.html',{'form':form})

def sell_property(request):
    return render(request,'home/sell.html')


def rent_property(request):
    return render(request, 'home/rent.html')

def rental_property_view(request):
    if request.method == 'POST':
        form = RentalPropertyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # به صفحه موفقیت هدایت می‌شود
    else:
        form = RentalPropertyForm()

    return render(request, 'home/RentalProperty.html',{'form': form})

def property_requst_view(request):
    if request.method == 'POST':
        form = RentalPropertyRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('درخواست شما با موفقیت ثبت شد.')
        else:
            return render(request, 'home/propertyrequest.html', {'form': form})
    else:
        form = RentalPropertyRequestForm()

    return render(request, 'home/propertyrequest.html', {'form': form})

