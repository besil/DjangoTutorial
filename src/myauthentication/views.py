from django.contrib.auth.models import User
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.base import View
from pprint import pprint

from myauthentication.forms import UserForm


# Create your views here.
def index(request):
    context = {"reg_form":UserForm(), "login_form":UserForm()}
    if 'message' in request.session:
        mex = request.session['message']
        del request.session['message']
        context['message'] = mex
    
    return render(request, "myauthentication/index.html", context)

class MyRegister(View):
    def post(self, request):
        uf = UserForm(request.POST)
        if uf.is_valid():
            name = uf.cleaned_data['name']
            pwd  = uf.cleaned_data['password']
            u = User.objects.create_user(name, "", pwd)
            request.session['message'] = "Registration completed"
            return redirect('index')

class MyLogin(View):
    pass