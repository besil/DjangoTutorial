from django.shortcuts import render
from django.http.response import HttpResponse
from django.views.generic.base import View

# Create your views here.
def index(request):
    return render(request, "myauthentication/index.html")

class MyRegister(View):
    def post(self, request):
        return HttpResponse("OK")

class MyLogin(View):
    pass