from django.http import HttpResponse
from django.template import loader

from django.views import View


def index(request):
    return HttpResponse("Hello, world. You're at the login page.")

class LoginClass(View):
    def get(self,request):
        template = loader.get_template('login/index.html')
        return HttpResponse(template.render(request))