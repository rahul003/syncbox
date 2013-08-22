from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from organizations.backends import invitation_backend
from django.contrib.auth.decorators import login_required

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blob.views.home', name='home'),
    # url(r'^blob/', include('blob.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('userena.urls')),
    url(r'^messages/', include('userena.contrib.umessages.urls')),
    (r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^', include('accum.urls')),
    url(r'^invitations/', include(invitation_backend().get_urls())),
    url(r'^upload/', include('fileupload.urls')),
    url(r'^orgs/', include('organizations.urls')),
    url(r'^groups/',include('search.urls'))
)

# Add media and static files
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#urlpatterns += patterns('',
#        url(r'^media/(.*)$', 'django.views.static.serve', {
#            'document_root': settings.MEDIA_ROOT,
#        }),
#   )