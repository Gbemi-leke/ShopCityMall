from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.views.generic import ListView

# from Olamide.frontend.models import *
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from frontend.models import *
from backend.forms import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# for sending mail import
from django.conf import settings
from django.core import mail
from django.template.loader import render_to_string
from django.contrib import messages
from django.utils.html import strip_tags
# end

# Create your views here.

def index(request):
    blogs = Blog.objects.order_by('-blog_date')[:6]
    restaurant = Restaurant.objects.order_by('-date')[:4]
    fashion = Fashion.objects.order_by('-date')[:4] 
    if request.method == 'POST':
        subscribe_form = SubscribeForm(request.POST)
        if subscribe_form.is_valid():
            subscribe_form = subscribe_form.save(commit=False)
            subscribe_form.user = request.user
            subscribe_form.save()
            messages.success(request, 'Add successfully.')
            return redirect('index')
    else:
        subscribe_form = SubscribeForm()
    return render(request, 'frontend/index.html', {'wears':fashion,'blog':blogs, 'restaurant':restaurant, 'subscribe_form':subscribe_form})


def about(request):
    if request.method == 'POST':
        subscribe_form = SubscribeForm(request.POST)
        if subscribe_form.is_valid():
            subscribe_form = subscribe_form.save(commit=False)
            subscribe_form.user = request.user
            subscribe_form.save()
            messages.success(request, 'Add successfully.')
            return redirect('frontend:about')
    else:
        subscribe_form = SubscribeForm()
    return render(request, 'frontend/about.html', {'subscribe_form':subscribe_form})

def foods(request):
    restaurant = Restaurant.objects.order_by('-date')
    if request.method == 'POST':
        subscribe_form = SubscribeForm(request.POST)
        if subscribe_form.is_valid():
            subscribe_form = subscribe_form.save(commit=False)
            subscribe_form.user = request.user
            subscribe_form.save()
            messages.success(request, 'Add successfully.')
            return redirect('frontend:foods')
    else:
        subscribe_form = SubscribeForm()
    return render(request, 'frontend/foods.html', {'restaurant':restaurant,'subscribe_form':subscribe_form})

def phones(request):
    gadgets=Gadgets.objects.order_by('-date')
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
    return render(request, 'frontend/phones.html', {'gad':gadgets,'subscribe_form':subscribe_form})

def phone_details(request, phones_id):
    phone_detail =Gadgets.objects.get(id=phones_id)
    if request.method == 'POST':
        subscribe_form = SubscribeForm(request.POST)
        if subscribe_form.is_valid():
            subscribe_form = subscribe_form.save(commit=False)
            subscribe_form.user = request.user
            subscribe_form.save()
            messages.success(request, 'Add successfully.')
            return redirect('frontend:wears')
    else:
        subscribe_form = SubscribeForm()
    return render(request, 'frontend/phone_details.html', {'det':phone_detail, 'subscribe_form':subscribe_form})

def wears(request):
    fashion = Fashion.objects.order_by('-date')
    if request.method == 'POST':
        subscribe_form = SubscribeForm(request.POST)
        if subscribe_form.is_valid():
            subscribe_form = subscribe_form.save(commit=False)
            subscribe_form.user = request.user
            subscribe_form.save()
            messages.success(request, 'Add successfully.')
            return redirect('frontend:wears')
    else:
        subscribe_form = SubscribeForm()
    return render(request, 'frontend/wears.html', {'wears':fashion,'subscribe_form':subscribe_form})

def wears_details(request, wears_id):
    wears_detail =Fashion.objects.get(id=wears_id)
    if request.method == 'POST':
        subscribe_form = SubscribeForm(request.POST)
        if subscribe_form.is_valid():
            subscribe_form = subscribe_form.save(commit=False)
            subscribe_form.user = request.user
            subscribe_form.save()
            messages.success(request, 'Add successfully.')
            return redirect('frontend:wears')
    else:
        subscribe_form = SubscribeForm()
    return render(request, 'frontend/wears_details.html', {'det':wears_detail, 'subscribe_form':subscribe_form})

def cakes(request):
    pastries=Pastries.objects.order_by('-date')
    if request.method == 'POST':
        subscribe_form = SubscribeForm(request.POST)
        if subscribe_form.is_valid():
            subscribe_form = subscribe_form.save(commit=False)
            subscribe_form.user = request.user
            subscribe_form.save()
            messages.success(request, 'Add successfully.')
            return redirect('frontend:cakes')
    else:
        subscribe_form = SubscribeForm()
    return render(request, 'frontend/cakes.html', {'cake':pastries,'subscribe_form':subscribe_form})

def cake_details(request, cake_id):
    cake_detail =Pastries.objects.get(id=cake_id)
    if request.method == 'POST':
        subscribe_form = SubscribeForm(request.POST)
        if subscribe_form.is_valid():
            subscribe_form = subscribe_form.save(commit=False)
            subscribe_form.user = request.user
            subscribe_form.save()
            messages.success(request, 'Add successfully.')
            return redirect('frontend:wears')
    else:
        subscribe_form = SubscribeForm()
    return render(request, 'frontend/cake_details.html', {'det':cake_detail, 'subscribe_form':subscribe_form})


def contact(request):
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if  contact_form.is_valid():
            contact_form = contact_form.save(commit=False)
            contact_form.user = request.user
            contact_form.save()
            messages.success(request, 'Your message has been sent. Thank you!')
            return redirect('frontend:contact')
    else:
        contact_form =ContactForm()
    if request.method == 'POST':
        subscribe_form = SubscribeForm(request.POST)
        if subscribe_form.is_valid():
            subscribe_form = subscribe_form.save(commit=False)
            subscribe_form.user = request.user
            subscribe_form.save()
            messages.success(request, 'Add successfully.')
            return redirect('frontend:contact')
    else:
        subscribe_form = SubscribeForm()
    return render(request, 'frontend/contact.html', {'cont':contact_form,'subscribe_form':subscribe_form})

def blog(request):
    blogs = Blog.objects.order_by('-blog_date')[:6]
    if request.method == 'POST':
        subscribe_form = SubscribeForm(request.POST)
        if subscribe_form.is_valid():
            subscribe_form = subscribe_form.save(commit=False)
            subscribe_form.user = request.user
            subscribe_form.save()
            messages.success(request, 'Add successfully.')
            return redirect('frontend:blog')
    else:
        subscribe_form = SubscribeForm()
    return render(request, 'frontend/blog.html', {'blog':blogs, 'subscribe_form':subscribe_form})

def blog_details(request, detail_id):
    detail =Blog.objects.get(id=detail_id)
    return render(request, 'frontend/blog_details.html', {'det':detail})

def hostel(request):
    if request.method == 'POST':
        subscribe_form = SubscribeForm(request.POST)
        if subscribe_form.is_valid():
            subscribe_form = subscribe_form.save(commit=False)
            subscribe_form.user = request.user
            subscribe_form.save()
            messages.success(request, 'Add successfully.')
            return redirect('frontend:hostel')
    else:
        subscribe_form = SubscribeForm()
    return render(request, 'frontend/hostel.html', {'subscribe_form':subscribe_form})


def payment(request):
    return render(request, 'frontend/payment.html')
