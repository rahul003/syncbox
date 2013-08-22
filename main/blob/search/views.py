# Create your views here
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
import os, tempfile, zipfile
from django.core.servers.basehttp import FileWrapper

from django.contrib.auth.models import User, UserManager,Group
from fileupload.models import Picture
from django.db.models import Q

@login_required
def showlist(request):
    pictures = Group.objects.filter(user__id=request.user.id)
    return render(request, 'search/groups.html', {'pictures': pictures})
@login_required
def create(request):
	#
	cre = Group.objects.create(name=request.GET.get('pq'))

	g = Group.objects.get(name=request.GET.get('pq')) 

	g.user_set.add(request.user)
	#useraccessed=User.objects.get(username__exact="demo")
	#g.user_set.add(useraccessed)
	#user=User.objects.get(id=request.user.id)
	cre.save()
	#user.groups.add(name=request.GET.get('pq'))
	pictures = Group.objects.filter(user__id=request.user.id)
	return render(request , 'search/groups.html', {'pictures': pictures})

def add(request):

	pictures = Group.objects.filter(user__id=request.user.id)
	#g = Group.objects.get(name=request.GET.get('grouppp')) 
	#g.user_set.add(request.GET.get('userrr'))
	return render(request , 'search/addtogroup.html', {'pictures': pictures} )


def adduser(request):

	
	#g = Group.objects.get(name=request.GET.get('grouppp')) 
	
	#useraccessed=User.objects.get(name=request.GET.get('userrr'))
	#g.user_set.add(useraccessed)
	#useraccessed=User.objects.get(name=request)
	g = Group.objects.get(name=request.GET.get('grouppp')) 
	useraccessed=User.objects.get(username="demo")
	g.user_set.add(useraccessed)
	pictures = Group.objects.filter(user__id=request.user.id)
	return render(request , 'search/addtogroup.html', {'pictures': pictures} )
