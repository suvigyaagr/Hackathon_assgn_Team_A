from django.http import HttpResponse, HttpResponseRedirect
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
        possible_passkey = [i.u_pass for i in User.objects.filter(u_id=user_name)]
        if password in possible_passkey:
            return redirect('charchitra:video_list', id=user_name)
        else:
            return HttpResponse("User not found")
