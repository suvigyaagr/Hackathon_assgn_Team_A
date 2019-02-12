from django.conf.urls import url

from . import views


app_name = 'charchitra'
urlpatterns = [
    url(r'^$',views.dashboard, name='dashboard')
]