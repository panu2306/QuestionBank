from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .forms import UserRegisterForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account Created for {username}!!!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', context= {'form': form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')

# TYPES OF django.contrib.messages: 
#1. error
#2. success
#3. warning
#4. debug
#5. info