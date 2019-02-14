from django.conf.urls import url

from . import views


app_name = 'charchitra'
urlpatterns = [    
    # url(r'^abc$',views.ListVideoView.as_view(), name='list_video'),
    url(r'^@(?P<user_id>\w+)/dashboard/$',views.dashboard, name='dashboard'),
    url(r'^@(?P<user_id>\w+)/video/$', views.VideoListView, name='video_list'),
    url(r'^@(?P<user_id>\w+)/video/(?P<video_id>\d+)/', views.VideoDetailView, name='video_detail'),
    url(r'^@(?P<user_id>\w+)/videopack/$', views.VideoPackListView, name='video_pack_list'),
    url(r'^@(?P<user_id>\w+)/$', views.UserProfileView, name='user_profile'),
    # # the line below is a test url
    # url(r'^videopack/$', views.VideoPackListView, name='video_list'),
]