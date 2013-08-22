from django.db import models
from django.contrib.auth.models import User, UserManager
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

def uploadmodel_file_upload_to(instance, filename):
    y="blob/media/pictures/%s"%instance.user.username
    if(y in filename):
        filename = filename.replace(y, "")
    return 'pictures/%s/%s' % (instance.user.username, filename)

class Picture(models.Model):

    # This is a small demo using just two fields. The slug field is really not
    # necessary, but makes the code simpler. ImageField depends on PIL or
    # pillow (where Pillow is easily installable in a virtualenv. If you have
    # problems installing pillow, use a more generic FileField instead.

    #file = models.FileField(upload_to="pictures")
    user = models.ForeignKey('auth.user')
    file = models.FileField(upload_to=uploadmodel_file_upload_to)
    slug = models.SlugField(max_length=50, blank=True)
    #content_type = models.ForeignKey(ContentType)
    #object_id = models.PositiveIntegerField()
    #content_object = generic.GenericForeignKey('content_type', 'object_id')

    def __unicode__(self):
        return self.file.name

    @models.permalink
    def get_absolute_url(self):
        return ('upload-new', )

    def save(self, *args, **kwargs):
        self.slug = self.file.name
        super(Picture, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.file.delete(False)
        super(Picture, self).delete(*args, **kwargs)
