from django.contrib.postgres.search import SearchQuery, SearchVector, SearchRank
from django.shortcuts import render
from django.views import View

from django.views import generic

from django.http import HttpResponse
from .models import *

# Create your views here.
def dashboard(request):
	return HttpResponse("Welcome")

	
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




class VideoDetailView(generic.DetailView):
	model = Video
	template_name = 'charchitra/detail.html'


class VideoDetailView(View):

	def get(self,request):
		video_dict={"v_name":"Toy story",
					"description":"Andy's favourite toy, Woody, is worried that after Andy receives his birthday gift, a new toy called Buzz Lightyear, his importance may get reduced. He thus hatches a plan to eliminate Buzz.",
					"url":"https://www.youtube.com/embed/tgbNymZ7vqY",
					}

		return render(request,'charchitra/video_detail.html',{'video':video_dict})