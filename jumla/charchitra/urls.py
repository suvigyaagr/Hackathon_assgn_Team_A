from django.conf.urls import url

from . import views


app_name = 'charchitra'
urlpatterns = [    
    # url(r'^abc$',views.ListVideoView.as_view(), name='list_video'),
    url(r'^dashboard/$',views.dashboard, name='dashboard'),
    url(r'^video/$', views.VideoListView.as_view(), name='video_list'),
    url(r'^video/(?P<pk>\d+)/$', views.VideoDetailView.as_view(), name = 'video_detail'),

    url(r'^videodt/$', views.VideoDetailView.as_view(), name = 'video_detail'),
]