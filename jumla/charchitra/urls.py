from django.conf.urls import url

from . import views


app_name = 'charchitra'
urlpatterns = [    
    # url(r'^abc$',views.ListVideoView.as_view(), name='list_video'),
    url(r'^dashboard/(?P<user_id>\w+)/$',views.dashboard, name='dashboard'),
    url(r'^video/(?P<user_id>\w+)/$', views.VideoListView, name='video_list'),
    url(r'^video/(?P<user_id>\w+)/(?P<video_id>\d+)/', views.VideoDetailView, name='video_detail'),
    url(r'^videopack/(?P<user_id>\w+)/$', views.VideoPackListView, name='video_pack_list'),
    url(r'^(?P<user_id>\w+)/$', views.UserProfileView, name='user_profile'),
    # # the line below is a test url
    # url(r'^videopack/$', views.VideoPackListView, name='video_list'),
]