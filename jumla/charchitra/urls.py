from django.conf.urls import url

from . import views


app_name = 'charchitra'
urlpatterns = [    
    # url(r'^abc$',views.ListVideoView.as_view(), name='list_video'),
    url(r'^dashboard/$',views.dashboard, name='dashboard'),
    url(r'^video/$', views.VideoListView, name='video_list'),
    url(r'^video/(?P<video_id>\d+)/$', views.VideoDetailView, name = 'video_detail'),
    url(r'^videopack/$', views.VideoPackListView, name='video_pack_list'),
]