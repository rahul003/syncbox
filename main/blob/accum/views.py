from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
import os, tempfile, zipfile
from django.core.servers.basehttp import FileWrapper
from django.core.mail import send_mail
import time

from fileupload.models import Picture
from django.db.models import Q
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
import os, tempfile, zipfile
from os.path import expanduser
from django.core.servers.basehttp import FileWrapper
from fileupload.models import Picture
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
import json
from collections import defaultdict
import re
from django.utils import simplejson
import unicodedata
from django.core.files import File
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import User, UserManager

#@login_required
def home(request):
    pictures = Picture.objects.filter(user__id=request.user.id)
    return render(request, 'accum/home.html', {'pictures': pictures})

"""Added for search operation using 'Q' for ANDed operations"""
@login_required
def share(request):
	if request.POST:
		li = request.POST.getlist('shpic')
		e = request.POST.get('email')	# share link with
		m = request.POST.get('body')
		m+= "\nHere are the files shared with you:\n"
		st=""
		print e
		print m
		for i in li:
			s='\n'+'http://172.16.26.79:8001'+i+'\n'
			print s
			st+=s
		m+=st 	# message
		time.sleep(7)
		send_mail('Shared Files', m, 'arpitdemo27@gmail.com', [e], fail_silently=False)
		print "mail sent"
		time.sleep(5)
		pictures={}
		mess="Files shared with "+e+": \n"+st
		return render(request, 'accum/share.html', {'pictures': pictures, 'mess':mess})
	if request.GET.get('sc'):
		mess={}
		pictures = Picture.objects.filter(Q(file__icontains=request.GET.get('sc')) & Q(user__id=request.user.id))
	else:
		mess={}
		pictures = {}#Picture.objects.filter(user__id=request.user.id)
	return render(request, 'accum/share.html', {'pictures': pictures, 'mess':mess})

@csrf_exempt
def desk(request):
	if request.method == 'POST':
		for item in request.POST:
			print item
		a = request.POST['username']
		b = request.POST['password']
		print a,b
		if request.POST['key']:
			c = request.POST['key']
			home = expanduser("~")
			g = open(home+'/.ssh/authorized_keys','a')
			g.write(c)
			g.close()
			print c
				
		#key = request.POST['']
		#print a
		#print b
		#response_data['result'] = 'failed'
		#response_data['message'] = 'You messed up'
		user = authenticate(username=a, password=b)
		message = ""
		if user is not None:
		    # the password verified for the user
		    if user.is_active:
		        message="User is valid, active and authenticated"
		    else:
		        message="The password is valid, but the account has been disabled!"
		else:
		    # the authentication system was unable to verify the username and password
		    message="The username and password were incorrect."
		resp = {'message': message,}
		return HttpResponse(json.dumps(resp), content_type="application/json")
		
@csrf_exempt
def desk2(request):
	if request.method == 'POST':
		pyJSON=defaultdict(dict)
		user=[]
		fi = open('/home/wall/log.txt','r')
		data = fi.read()
		fi.close()
		fo = open('/home/wall/log.txt','w')
		fo.write(data.replace('\x00', ''))
		fo.close()
		f=open('/home/wall/log.txt','r')



		for line in f:
			line=line[:-1]
			tmp = re.search(r'(.*).unison.tmp', line, re.M)
			if tmp:
				continue
		#	for item in [' CREATE ',' ATTRIB ',' CREATE,ISDIR ',' MOVED_TO,ISDIR ',' MOVED_FROM,ISDIR ',' MOVED_FROM ',' MOVED_TO ',' MOVE_SELF ',' ATTRIB,ISDIR ']:
			a = re.search(r'(.*) CREATE (.*)', line, re.M)
			b = re.search(r'(.*) MOVED_TO (.*)', line, re.M)
			#print line
			userstart = line[42:]
			user = userstart.split('/')[0]
			
			if a:
				line = line.replace(' CREATE ','')
				
				try:
					pyJSON[user]['create'].append(line)
				except:
					pyJSON[user]['create'] = list()
					pyJSON[user]['create'].append(line)
			if b:
				line = line.replace(' MOVED_TO ','')
				try:
					pyJSON[user]['create'].append(line)
				except:
					pyJSON[user]['create'] = list()
					pyJSON[user]['create'].append(line)
			c = re.search(r'(.*) MOVED_FROM (.*)', line, re.M)
			d = re.search(r'(.*) DELETE (.*)', line, re.M)
			if c:
				line = line.replace(' MOVED_FROM ','')
				
				userstart = line[42:]
				user = userstart.split('/')[0]
				try:
					pyJSON[user]['delete'].append(line)
				except:
					pyJSON[user]['delete'] = list()
					pyJSON[user]['delete'].append(line)
			if d:
				line = line.replace(' DELETE ','')
				#if item == ' CREATE ' or item == ' MOVED_TO ':
				userstart = line[42:]
				user = userstart.split('/')[0]
				try:
					pyJSON[user]['delete'].append(line)
				except:
					pyJSON[user]['delete'] = list()
					pyJSON[user]['delete'].append(line)
		f.close()
		print pyJSON
		for item in pyJSON:
			u = User.objects.get(username = item)
			print u
			
			try:
				for a in pyJSON[item]['create']:
					p = Picture()
					p.file.name=a[33:]
					print a[33:]
					po=Picture(user=u, file=p.file)
					po.save()
			except:	
				print "no"
			try:
				for a in pyJSON[item]['delete']:
					p = Picture()
					p.file.name=a[33:]
					print a[33:]
					# po=Picture(user=u, file=p.file)
					b = Picture.objects.get(user=u,file=p.file)
					b.delete()
					print file
					print "isdeleted"
			except:
				print "no"

def validateEmail( email ):
    from django.core.validators import validate_email
    from django.core.exceptions import ValidationError
    try:
        validate_email( email )
        return True
    except ValidationError:
        return False
#@login_required
#def share(request):
#	pictures={}
	#if request.POST:
	#	send_mail('Subject here', 'Here is the message.', 'from@example.com', ['to@example.com'], fail_silently=False)
#	return render(request, 'accum/share.html', {'pictures':pictures})
#@login_required
#def send_file(request):user__id=request.user.id && 
#    """                                  file__contains='images'                                       
#    Send a file through Django without loading the whole file into              
#   memory at once. The FileWrapper will turn the file object into an           
#    iterator for chunks of 8KB.                                                 
#    """
#    filename = __file__ # Select your file here.                                
#    wrapper = FileWrapper(file(filename))
#    response = HttpResponse(wrapper, content_type='text/plain')
#    response['Content-Length'] = os.path.getsize(filename)
#    return response

#@login_required
#def send_zipfile(request):
#    """                                                                         
#    Create a ZIP file on disk and transmit it in chunks of 8KB,                 
#    without loading the whole file into memory. A similar approach can          
#    be used for large dynamic PDF files.                                        
#    """
#    temp = tempfile.TemporaryFile()
#    archive = zipfile.ZipFile(temp, 'w', zipfile.ZIP_DEFLATED)
#    for index in range(10):
#        filename = __file__ # Select your files here.                           
#        archive.write(filename, 'file%d.txt' % index)
#    archive.close()
#    wrapper = FileWrapper(temp)
#    response = HttpResponse(wrapper, content_type='application/zip')
#    response['Content-Disposition'] = 'attachment; filename=test.zip'
#    response['Content-Length'] = temp.tell()
#    temp.seek(0)
#    return response