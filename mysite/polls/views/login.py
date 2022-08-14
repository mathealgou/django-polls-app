from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

def login(request):
	return render(request, 'polls/login.html')

def login_submit(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        auth_login(request, user)
        return HttpResponseRedirect(reverse('index'))
    else:
        HttpResponse('<h1>Invalid username or password</h1>')

def logout(request):
	auth_logout(request)
	return HttpResponseRedirect(reverse('index'))