from django.conf.urls.defaults import *
from fileupload.views import PictureCreateView, PictureDeleteView
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',
    (r'^new/$', login_required(PictureCreateView.as_view()), {}, 'upload-new'),
    (r'^delete/(?P<pk>\d+)$', login_required(PictureDeleteView.as_view()), {}, 'upload-delete'),
)

