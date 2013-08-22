from fileupload.models import Picture
from django.contrib import admin

class PictureAdmin(admin.ModelAdmin):
    fields = ['user', 'file']
    search_fields = ['file']
admin.site.register(Picture, PictureAdmin)