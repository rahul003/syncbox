from django.conf.urls import patterns, url

urlpatterns = patterns('',
	url(r'^$', 'accum.views.home', name='home'),
	url(r'^share/', 'accum.views.share', name='share'),# Url for search operation
	url(r'^desk/', 'accum.views.desk', name='desk'),
	url(r'^desk2/', 'accum.views.desk2', name='desk2'),
	#url(r'^share/', 'accum.views.share', name='share'),
	#url(r'^(?P<sc>\d+)/search/$', 'accum.views.search' , name='search1')
	)