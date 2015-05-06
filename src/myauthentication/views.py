from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from django.views.generic.base import View
from myauthentication.forms import UserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)

def index(request):
    context = {"reg_form":UserForm(), "login_form":UserForm()}
    if 'message' in request.session:
        mex = request.session['message']
        del request.session['message']
        context['message'] = mex
    
    return render(request, "myauthentication/index.html", context)

class MyHome(LoginRequiredMixin, View):
    def get(self, request):
        username = request.session['user_data']
        print username
        context = { "nome_utente": username }
        return render(request, "myauthentication/home.html", context)

class MyRegister(View):
    def post(self, request):
        uf = UserForm(request.POST)
        try:
            if uf.is_valid():
                name = uf.cleaned_data['name']
                mail = name
                pwd  = uf.cleaned_data['password']
                User.objects.create_user(name, mail, pwd)
                request.session['message'] = "Registration completed"
                return redirect('index')
        except Exception: pass
        
        request.session['message'] = "An error occured"
        return redirect('index')

class MyLogout(View):
    def get(self, request):
        logout(request)
        return redirect('index')

class MyLogin(View):
    def post(self, request):
        uf = UserForm(request.POST)
        user = None
        if uf.is_valid():
            name        = uf.cleaned_data['name']
            mail        = name
            password    = uf.cleaned_data['password'] 
            user = authenticate(username=name, password=password, mail=mail)
        
        if user is not None:
            if user.is_active:
                login(request, user)
                request.session['user_data'] = user.username
                return redirect("home")
            else:
                request.session['message'] = "An error in login"
                return redirect('index')
        else:
            request.session['message'] = "Login error"
            return redirect('index')
            
            
            
