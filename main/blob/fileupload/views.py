from fileupload.models import Picture
from django.views.generic import CreateView, DeleteView, ListView
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import simplejson
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User, UserManager

from django.conf import settings

def response_mimetype(request):
    if "application/json" in request.META['HTTP_ACCEPT']:
        return "application/json"
    else:
        return "text/plain"


class PictureCreateView(CreateView):
    model = Picture

    def get(self, request):
        if request.is_ajax():
            pictures = Picture.objects.filter(user__id=self.request.user.id)
            data = []
            user = self.request.user
            for p in pictures:
                data += [{'name': p.file.name[8:], 'url': p.file.url, 'thumbnail_url': p.file.url, 'delete_url': reverse('upload-delete', args=[p.id]), 'delete_type': "DELETE"}]
            response = JSONResponse(data, {}, response_mimetype(self.request))
            response['Content-Disposition'] = 'inline; filename=files.json'
            return response
        else:
            return render(self.request, 'fileupload/picture_form.html')

    def form_valid(self, form):
        #pictures = Picture.objects.filter(user__id=self.request.user.id)
        #data = []
        #for p in pictures:
        #    data += [{'name': p.file.name, 'url': settings.MEDIA_URL  + p.file.name.replace(" ", "%20"), 'thumbnail_url': settings.MEDIA_URL  + p.file.name.replace(" ", "%20"), 'delete_url': reverse('upload-delete', args=[p.id]), 'delete_type': "DELETE"}]
        self.object = form.save()
        f = self.request.FILES.get('file')
        user = self.request.user
        data = [{'name': f.name, 'url': settings.MEDIA_URL + "pictures/"+ user.username + "/" + f.name.replace(" ", "%20"), 'thumbnail_url': settings.MEDIA_URL + "pictures/"+ user.username + "/" + f.name.replace(" ", "%20"), 'delete_url': reverse('upload-delete', args=[self.object.id]), 'delete_type': "DELETE"}]
        response = JSONResponse(data, {}, response_mimetype(self.request))
        response['Content-Disposition'] = 'inline; filename=files.json'
        return response

    #def get_form(self, form):
    #    pictures = Picture.objects.filter(user__id=self.request.user.id)
    #    return render(self.request, 'fileupload/picture_form.html', {'pictures': pictures})


class PictureDeleteView(DeleteView):
    model = Picture

    def get(self, request, *args, **kwargs):
        return HttpResponseRedirect('/upload/new')

    def delete(self, request, *args, **kwargs):
        """
        This does not actually delete the file, only the database record.  But
        that is easy to implement.
        """
        self.object = self.get_object()
        #if self.object.user.id != self.request.user.id:
        #    return HttpResponseRedirect('/upload/new')
        self.object.delete()
        if request.is_ajax():
            response = JSONResponse(True, {}, response_mimetype(self.request))
            response['Content-Disposition'] = 'inline; filename=files.json'
            return response
        else:
            return HttpResponseRedirect('/upload/new')

class JSONResponse(HttpResponse):
    """JSON response class."""
    def __init__(self,obj='',json_opts={},mimetype="application/json",*args,**kwargs):
        content = simplejson.dumps(obj,**json_opts)
        super(JSONResponse,self).__init__(content,mimetype,*args,**kwargs)

#@login_required
#def download(request):
#    pictures = Picture.objects.filter(user__id=request.user.id)
#    return render(request, 'fileupload/picture_form.html', {'pictures': pictures})