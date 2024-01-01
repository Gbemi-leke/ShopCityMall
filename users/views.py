from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

# Models
from django.contrib import messages
from users.models import *
from users.forms import *

# signUp
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_text
from django.db import IntegrityError
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
# from backend.tokens import account_activation_token
# from .tokens import account_activation_token
from django.template.loader import render_to_string
#end

# Create your views here.


@login_required(login_url='/backend/login/')
def user_profile(request):
    return render(request, 'backend/user_profile.html')

@login_required(login_url='/backend/login/')
def edit_profile(request):
    if request.method == 'POST':
        edit_form = EditUserForm(request.POST,request.FILES, instance=request.user,)
        if edit_form.is_valid():
            edit_form.save()
            messages.success(request, 'User edited successfully.')
            # return edit_form.save()

        else:
            messages.success(request, 'User edited unsuccessfully.')
            
    else:
        edit_form = EditUserForm(instance=request.user)
    return render(request, 'backend/edit_profile.html', {'edit_form':edit_form})