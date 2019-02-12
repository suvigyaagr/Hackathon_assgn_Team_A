from django.conf.urls import url

from . import views


app_name = 'charchitra'
urlpatterns = [
    url(r'^$',views.ListVideoView.as_view(), name='video_list'),
    url(r'^dashboard/$',views.dashboard, name='dashboard'),
]