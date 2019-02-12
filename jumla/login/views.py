from django.http import HttpResponse
from django.template import loader
from django.template.loader import get_template
from django.views import View
from django.shortcuts import render


def index(request):
    return HttpResponse("Hello, world. You're at the login page.")

class LoginClass(View):
    def get(self,request):
        return render(request,'login/index.html')

    def post(self,request):
        print(request.POST.get("Username"))
        print(request.POST.get("Password"))
        return HttpResponse("got it fam")
