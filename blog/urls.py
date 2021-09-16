from django.conf.urls import url
from . import views


app_name = 'blog'

urlpatterns = [
	url(r'^delete/(?P<delete_id>.*)', views.delete, name='delete'),
	url(r'^update/(?P<update_id>.*)', views.update, name='update'),
	url(r'^create/$', views.create, name='create'),
	url(r'^$', views.list, name='list'),
]