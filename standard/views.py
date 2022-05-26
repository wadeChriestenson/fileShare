from django.shortcuts import render, redirect
from django.contrib.auth import logout as django_logout
from django.conf import settings
from django.contrib.auth.decorators import login_required, permission_required
from standard.forms import FileForm
from standard.models import userFiles
from django.contrib import messages
import pandas as pd


# Create your views here.
def index(request):
    return render(request, 'index.html', {})


@login_required
def logout(request):
    django_logout(request)
    domain = settings.SOCIAL_AUTH_AUTH0_DOMAIN
    client_id = settings.SOCIAL_AUTH_AUTH0_KEY
    return_to = 'http://127.0.0.1:8000'  # this can be current domain
    return redirect(f'https://{domain}/v2/logout?client_id={client_id}&returnTo={return_to}')


@login_required
def user_is_true(request):
    from .models import User
    userName = User.objects.all()
    print(userName)
    user = userName[2]
    return render(request, 'user.html', {'user': user})


@login_required
def upload(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.clean())
            form.clean()
            form.save()
            messages.success(request, 'File Uploaded Successfully')
    form = FileForm()
    return render(request, 'upload_files.html', {'form': form})


@login_required
def download(request):
    files = userFiles.objects.all().values().order_by('file_name')
    from .models import User
    userName = User.objects.values()
    print(userName[1]['username'])
    return render(request, 'download_files.html', {'files': files})
