from django.conf.urls import url

from . import views


app_name = 'login'
urlpatterns = [
    #url(r'^$', views.index, name='index'),
    url(r'$',views.LoginClass.as_view(),name='login')
]