from django.http import HttpResponse
from django.template import loader
from django.template.loader import get_template
from django.views import View
from django.shortcuts import render, redirect
from django.views import View
from .models import User


def index(request):
    return HttpResponse("Hello, world. You're at the login page.")

class LoginClass(View):
    def get(self,request):
        return render(request,'login/index.html')

    def post(self,request):
        user_name = request.POST.get("username")
        password = request.POST.get("password")
        print(User.objects.get(u_id=user_name))
        if password == User.objects.get(u_id=user_name):
            return redirect('/charchitra/')