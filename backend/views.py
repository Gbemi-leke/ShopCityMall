from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core import mail
from django.views.generic import ListView
from django.contrib.auth import update_session_auth_hash
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.edit import UpdateView

# Models
from django.contrib import messages
from frontend.models import *
from backend.forms import *
from payments.models import *
from users.models import *
from users.forms import *

# Password Reset
from django.conf import settings
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import BadHeaderError, send_mail
from django.db.models import Q
from django.http import HttpResponse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
 #  end

def login_view(request):
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        password = request.POST.get('password')

        # Authenticate the user
        user = authenticate(request, username=user_name, password=password)  

        # If the user is authenticated, log them in and redirect to the homepage
        if user is not None:
            login(request, user)
            # if user.account_type == 'admin':
            #     return redirect('backend/user_profile.html')
            # elif user.account_type == 'vendor':
            #     return redirect('backend/user_profile.html')
            # elif user.account_type == 'user':
            #     return redirect('backend/user_profile.html')
            return render(request, 'backend/index.html')
        else:
            messages.error(request, 'Invalid username or password')  
    return render(request, 'frontend/login.html')



def register(request):
    if request.method  == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.user_name = form.cleaned_data.get('user_name')
            user.first_name = form.cleaned_data.get('first_name')
            user.email = form.cleaned_data.get('email')
            user.account_type = form.cleaned_data.get('account_type')
            messages.success(request, 'User Registered, you can can  proceed to Log in page')
    else:
        form = RegisterForm()
    return render(request, 'frontend/reg.html', {'reg':form})

@login_required(login_url='/backend/login/')
def logout_view(request):
    logout(request)
    return redirect('index')

@login_required(login_url='/backend/login/')
def dashboard(request):
    list_all_blog = Blog.objects.filter(user=request.user)[:4]
    return render(request, 'backend/index.html', {'list_blog':list_all_blog})

@login_required(login_url='/backend/login/')
def message(request):
    contact = Contact.objects.all()
    return render(request, 'backend/contact.html', {'contact':contact})

@login_required(login_url='/backend/login/')
def newsletter(request):
    newsletter = SubscribeModel.objects.order_by('-timestamp')
    return render(request, 'backend/newsletter.html', {'newsletter':newsletter})

@login_required(login_url='/backend/login/')
def change_password(request):
    if request.method == 'POST':
        change_password = PasswordChangeForm(data=request.POST,
        user=request.user)
        if change_password.is_valid():
            change_password.save()
            update_session_auth_hash(request, change_password.user)
            messages.success(request, 'Password changed successfully.')
    else:
        change_password = PasswordChangeForm(user=request.user)
    return render(request, 'backend/change_password.html', {'pass_key':change_password})


def password_reset_request(request):
    if request.method == "POST":
        domain = request.headers['Host']
        password_reset_form = PasswordReset(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=data))
            # You can use more than one way like this for resetting the password.
            # ...filter(Q(email=data) | Q(username=data))
            # but with this you may need to change the password_reset form as well.
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "backend/password_reset_email.txt"
                    c = {
                        "email": user.email,
                        'domain': '127.0.0.1:8000/',
                        'site_name':'ALLINONE',
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject, email, 'josepholuwagbemi02@gmail.com', [user.email], fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    return redirect("/password_reset/done/")
    password_reset_form = PasswordReset()
    if request.method == 'POST':
        subscribe_form = SubscribeForm(request.POST)
        if subscribe_form.is_valid():
            subscribe_form = subscribe_form.save(commit=False)
            subscribe_form.user = request.user
            subscribe_form.save()
            messages.success(request, 'Upload successfully.')
            return redirect('frontend:password_reset_request')
    else:
        subscribe_form = SubscribeForm()
    return render(request=request, template_name="backend/password_reset.html",
                  context={"password_reset_form": password_reset_form,'subscribe_form':subscribe_form})

@login_required(login_url='/backend/login/')
def food(request):
    restaurant = Restaurant.objects.order_by('-date')
    return render(request, 'backend/food.html', {'restaurant':restaurant})

@login_required(login_url='/backend/login/')
def pastries(request):
    pastries = Pastries.objects.order_by('-date')
    return render(request, 'backend/pastries.html', {'pastries':pastries})

@login_required(login_url='/backend/login/')
def edit_pastries(request, pastries_id):
    pastries_post = get_object_or_404(Pastries, id=pastries_id)
    if request.method == 'POST':
        editpastries_form = EditPastriesForm(request.POST, request.FILES,instance=pastries_post)
        if editpastries_form.is_valid():
            editpastries_form = editpastries_form.save(commit=False)
            editpastries_form.user = request.user
            editpastries_form.save()
            messages.success(request, 'Successfully Edited.')
            editpastries_form = EditPastriesForm(instance=pastries_post)
            
    else:
        editpastries_form = EditPastriesForm(instance=pastries_post)
    return render(request, 'backend/edit_cakes.html', {'editpastries_form': editpastries_form})

@login_required(login_url='/backend/login/')
def delete_pastries(request, deletepastries_id):
    pastries_record = get_object_or_404(Pastries, id=deletepastries_id)
    pastries_record.delete()
    return redirect('backend:dashboard')

@login_required(login_url='/backend/login/')
def gadgets(request):
    gadgets = Gadgets.objects.order_by('-date')
    return render(request, 'backend/gadgets.html', {'gadgets':gadgets})

@login_required(login_url='/backend/login/')
def edit_gadgets(request, gadgets_id):
    gadgets_post = get_object_or_404(Gadgets, id=gadgets_id)
    if request.method == 'POST':
        editgadgets_form = EditGadgetsForm(request.POST, request.FILES,instance=gadgets_post)
        if editgadgets_form.is_valid():
            editgadgets_form = editgadgets_form.save(commit=False)
            editgadgets_form.user = request.user
            editgadgets_form.save()
            messages.success(request, 'Successfully Edited.')
            editgadgets_form = EditGadgetsForm(instance=gadgets_post)
            
    else:
        editgadgets_form = EditGadgetsForm(instance=gadgets_post)
    return render(request, 'backend/edit_phone.html', {'editgadgets_form': editgadgets_form})

@login_required(login_url='/backend/login/')
def delete_gadgets(request, deletegadgets_id):
    gadgets_record = get_object_or_404(Gadgets, id=deletegadgets_id)
    gadgets_record.delete()
    return redirect('backend:dashboard')


@login_required(login_url='/backend/login/')
def wears(request):
    wears = Fashion.objects.order_by('-date')
    return render(request, 'backend/wears.html', {'wears':wears})

@login_required(login_url='/backend/login/')
def add_gadgets(request):
    if request.method == 'POST':
        gadgets_form = GadgetsForm(request.POST, request.FILES)
        if gadgets_form.is_valid():
            gadgets_form = gadgets_form.save(commit=False)
            gadgets_form.user = request.user
            gadgets_form.save()
            messages.success(request, 'Upload successfully.')
            return redirect('backend:add_gadgets')
    else:
        gadgets_form = GadgetsForm()
    return render(request, 'backend/add_phone.html', {'gadgets_form': gadgets_form})


@login_required(login_url='/backend/login/')
def add_pastries(request):
    if request.method == 'POST':
        pastries_form = PastriesForm(request.POST, request.FILES)
        if pastries_form.is_valid():
            pastries_form = pastries_form.save(commit=False)
            pastries_form.user = request.user
            pastries_form.save()
            messages.success(request, 'Upload successfully.')
            return redirect('backend:add_pastries')
    else:
        pastries_form = PastriesForm()
    return render(request, 'backend/add_cakes.html', {'pastries_form': pastries_form})

@login_required(login_url='/backend/login/')
def add_wears(request):
    if request.method == 'POST':
        wears_form = FashionForm(request.POST, request.FILES)
        if wears_form.is_valid():
            wears_form = wears_form.save(commit=False)
            wears_form.user = request.user
            wears_form.save()
            messages.success(request, 'Upload successfully.')
            return redirect('backend:add_wears')
    else:
        wears_form = FashionForm()
    return render(request, 'backend/add_wears.html', {'wears_form': wears_form})

@login_required(login_url='/backend/login/')
def add_blog(request):
    if request.method == 'POST':
        blog_form = BlogForm(request.POST, request.FILES)
        if blog_form.is_valid():
            blog_form = blog_form.save(commit=False)
            blog_form.user = request.user
            blog_form.save()
            messages.success(request, 'Upload successfully.')
            return redirect('backend:add_blog')
    else:
        blog_form = BlogForm()
    return render(request, 'backend/add_blog.html', {'blog_form': blog_form})

@login_required(login_url='/backend/login/')
def edit_blog(request, post_id):
    blog_post = get_object_or_404(Blog, id=post_id)
    if request.method == 'POST':
        editblog_form = EditBlogForm(request.POST, request.FILES,instance=blog_post)
        if editblog_form.is_valid():
            editblog_form = editblog_form.save(commit=False)
            editblog_form.user = request.user
            editblog_form.save()
            messages.success(request, 'Successfully Edited.')
            editblog_form = EditBlogForm(instance=blog_post)
            
    else:
        editblog_form = EditBlogForm(instance=blog_post)
    return render(request, 'backend/edit_blog.html', {'editblog_form': editblog_form})

@login_required(login_url='/backend/login/')
def edit_wears(request, wears_id):
    wears_post = get_object_or_404(Fashion, id=wears_id)
    if request.method == 'POST':
        editwears_form = EditWearsForm(request.POST, request.FILES,instance=wears_post)
        if editwears_form.is_valid():
            editwears_form = editwears_form.save(commit=False)
            editwears_form.user = request.user
            editwears_form.save()
            messages.success(request, 'Successfully Edited.')
            editwears_form = EditWearsForm(instance=wears_post)
            
    else:
        editwears_form = EditWearsForm(instance=wears_post)
    return render(request, 'backend/edit_wears.html', {'editwears_form': editwears_form})

@login_required(login_url='/backend/login/')
def delete_wears(request, deletewears_id):
    wears_record = get_object_or_404(Fashion, id=deletewears_id)
    wears_record.delete()
    return redirect('backend:dashboard')

@login_required(login_url='/backend/login/')
def view_blog(request, view_id):
    post = Blog.objects.filter( id=view_id)
    return render(request, 'backend/view_blog.html', {'pst':post})


@login_required(login_url='/backend/login/')
def list_all_blog(request):
    list_all_blog = Blog.objects.order_by('-blog_date')[:20]
    return render(request, 'backend/list_all_blog.html', {'list_blog':list_all_blog})


@login_required(login_url='/backend/login/')
def delete_blog(request, delete_id):
    blog_record = get_object_or_404(Blog, id=delete_id)
    blog_record.delete()
    return redirect('backend:list_all_blog')

@login_required(login_url='/backend/login/')
def preview(request, agent):
    file = get_object_or_404(Blog, pk=agent)
    return render(request, 'backend/preview.html', {'post':file})
