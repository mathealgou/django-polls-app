from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.urls import reverse
from django.contrib import auth
from django.contrib.auth.models import User


def signup(request):
    return render(request, 'polls/signup.html')

def signup_submit(request):
    # print the request body
    print(request.POST["username"])
    print(request.POST["email"])
    print(request.POST["password"])
    User.objects.create_user(request.POST["username"], request.POST["email"], request.POST["password"])
    
    return HttpResponseRedirect(reverse('polls:index'))