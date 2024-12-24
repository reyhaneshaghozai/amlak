from django.shortcuts import render,redirect
from .forms import PropertyRequestForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

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
