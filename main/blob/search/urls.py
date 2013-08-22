from django.conf.urls.defaults import *
from django.views.generic.base import TemplateView
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

from userena import views as userena_views
from userena import settings as userena_settings
from django.conf.urls import patterns, url

urlpatterns = patterns('',
	url(r'^$', 'search.views.showlist', name='groups_list'),
	url(r'^create/', 'search.views.create', name='search'),
	url(r'^add/','search.views.add', name='addtogroup'),
	url(r'^fdsa/', 'search.views.adduser', name= 'addusertogroup')
	#url(r'^adduser/', 'search.views.adduser', name= 'adduser ' ),

	)