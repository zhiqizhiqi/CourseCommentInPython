from django.conf.urls import patterns, url, include

from userpage import views

urlpatterns = patterns('',
	url(r'^change/$', views.changeLecture),
)
