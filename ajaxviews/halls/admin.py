from django.contrib import admin
from .models import Hall, Video


class HallAdmin(admin.ModelAdmin):
    pass

admin.site.register(Hall, HallAdmin)



class VideoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Video, VideoAdmin)
