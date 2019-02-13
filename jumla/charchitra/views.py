from django.contrib.postgres.search import SearchQuery, SearchVector, SearchRank
from django.shortcuts import render, get_object_or_404
from django.views import View

from django.views import generic

from django.http import HttpResponse
from .models import *

# Create your views here.
def dashboard(request):
	return render(request, 'charchitra/dashboard.html')

	
# class ListVideoView(View):
#     def get(self,request):
#         # l=[{"title":"https://images-na.ssl-images-amazon.com/images/I/41kYaOc988L._SL500_AC_SS350_.jpg"},
#         #    {"title": "https://images-na.ssl-images-amazon.com/images/I/41kYaOc988L._SL500_AC_SS350_.jpg"},
#         #    {"title": "https://images-na.ssl-images-amazon.com/images/I/41kYaOc988L._SL500_AC_SS350_.jpg"},
#         #    {"title": "https://images-na.ssl-images-amazon.com/images/I/41kYaOc988L._SL500_AC_SS350_.jpg"}]

#         # l= [ "https://images-na.ssl-images-amazon.com/images/I/41kYaOc988L._SL500_AC_SS350_.jpg",
#         #      "https://images-na.ssl-images-amazon.com/images/I/41kYaOc988L._SL500_AC_SS350_.jpg",
#         #      "https://images-na.ssl-images-amazon.com/images/I/41kYaOc988L._SL500_AC_SS350_.jpg",
#         #      ]

#         l = [ { "title" : "https://images-na.ssl-images-amazon.com/images/I/41kYaOc988L._SL500_AC_SS350_.jpg" }]
#         return render(request,'charchitra/video_list.html',{'video_list':l})

      

# class VideoListView(generic.ListView):
# 	model = Video
# 	template_name = 'charchitra/video_list.html'

def VideoListView(request):
	video_list = Video.objects.all()
	print(video_list)
	video_price_list = VideoPrice.objects.all()
	print(video_price_list)
	template_name = 'charchitra/video_list.html'
	context = {
	'video_list' : video_list,
	'video_price_list' : video_price_list,
	}
	return render(request, template_name, context)

# 	def get_queryset(self):
# 		# qs = Video.objects.all()
# 		return Video.objects.filter(v_name__icontains=self.request.GET.get('search_data'))

# 	def get_queryset(self):
# 		# qs = Video.objects.all()
# 		word = self.request.GET.get('search_data')
# 		if word:
# 			return Video.objects.filter(v_name__icontains=word)
# 		else:
# 			return Video.objects.all()


def VideoDetailView(request, video_id):
	video_detail = get_object_or_404(Video, pk=video_id)
	print(video_detail)
	video_price_detail = VideoPrice.objects.filter(v_id=video_id)
	print(video_price_detail)
	template_name = 'charchitra/video_detail.html'
	context = {
		'video_detail' : video_detail,
		'video_price_detail' : video_price_detail,
	}
	return render(request, template_name, context)


def VideoPackListView(request):
	HttpResponse("Welcome to Video Packs.")


def user_profile(request):
	return render(request, 'charchitra/user_profile.html')
