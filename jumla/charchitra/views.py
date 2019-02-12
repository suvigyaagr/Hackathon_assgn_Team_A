from django.shortcuts import render
# from django.views import generics
from django.http import HttpResponse
from .models import *


# Create your views here.
def dashboard(request):
	return HttpResponse("Welcome")


class VideoView(generic.ListView):
	model = Video
	template_name = 'charchitra/video_list.html'

	def get_queryset(self):
		return Video.objects.all()


class