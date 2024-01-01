from django.shortcuts import render, redirect, get_object_or_404
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from payments.models import *
from frontend.models import *
from payments.forms import *
from backend.forms import *
from django.contrib import messages
from django.conf import settings

# Create your views here.

def initiate_payment(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        payment_form = PaymentForm(request.POST)
        if payment_form.is_valid():
            payment = payment_form.save()
            return render(request, 'backend/make_payment.html', {'payment':payment, 'paystack_public_key':settings.PAYSTACK_PUBLIC_KEY})
    else:
        payment_form = PaymentForm()

    if request.method == 'POST':
        subscribe_form = SubscribeForm(request.POST)
        if subscribe_form.is_valid():
            subscribe_form = subscribe_form.save(commit=False)
            subscribe_form.user = request.user
            subscribe_form.save()
            messages.success(request, 'Add successfully.')
            return redirect('frontend:phones')
    else:
        subscribe_form = SubscribeForm()
    return render(request, 'backend/initiate_payment.html', {'payment_form':payment_form,'subscribe_form':subscribe_form})
  
def verify_payment(request: HttpRequest, ref: str) -> HttpResponse:
    payment =get_object_or_404(Payment, ref=ref)
    verified = payment.verify_payment()
    if verified:
        messages.success(request, "verification Successful")
    else:
        messages.error(request, "verification Failed")
    
    if request.method == 'POST':
        subscribe_form = SubscribeForm(request.POST)
        if subscribe_form.is_valid():
            subscribe_form = subscribe_form.save(commit=False)
            subscribe_form.user = request.user
            subscribe_form.save()
            messages.success(request, 'Add successfully.')
            return redirect('frontend:phones')
    else:
        subscribe_form = SubscribeForm()
    return redirect('payments:initiate_payment', {'subscribe_form':subscribe_form})

