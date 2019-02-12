from django.shortcuts import render
from django.views import View

# from django.views import generics
from django.http import HttpResponse
from .models import *


# Create your views here.
class ListVideoView(View):
    def get(self,request):
        # l=[{"title":"https://images-na.ssl-images-amazon.com/images/I/41kYaOc988L._SL500_AC_SS350_.jpg"},
        #    {"title": "https://images-na.ssl-images-amazon.com/images/I/41kYaOc988L._SL500_AC_SS350_.jpg"},
        #    {"title": "https://images-na.ssl-images-amazon.com/images/I/41kYaOc988L._SL500_AC_SS350_.jpg"},
        #    {"title": "https://images-na.ssl-images-amazon.com/images/I/41kYaOc988L._SL500_AC_SS350_.jpg"}]

        # l= [ "https://images-na.ssl-images-amazon.com/images/I/41kYaOc988L._SL500_AC_SS350_.jpg",
        #      "https://images-na.ssl-images-amazon.com/images/I/41kYaOc988L._SL500_AC_SS350_.jpg",
        #      "https://images-na.ssl-images-amazon.com/images/I/41kYaOc988L._SL500_AC_SS350_.jpg",
        #      ]

        l = [ { "title" : "https://images-na.ssl-images-amazon.com/images/I/41kYaOc988L._SL500_AC_SS350_.jpg" }]
        return render(request,'index.html',{'bla':l})

      
def dashboard(request):
	return HttpResponse("Welcome")


class VideoView(generic.ListView):
	model = Video
	template_name = 'charchitra/video_list.html'

	def get_queryset(self):
		return Video.objects.all()


class