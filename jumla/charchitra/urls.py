from django.conf.urls import url

from . import views


app_name = 'charchitra'
urlpatterns = [
    url(r'^$',views.dashboard, name='dashboard'),
    url(r'^videos/$', views.VideoListView.as_view(), name='video-list'),
    url(r'^videos/(?P<pk>\d+)/$', views.VideoDetailView.as_view(), name = 'video-detail'),

]