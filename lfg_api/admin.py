from django.contrib import admin
from .models import VideoGame, UserProfile, Party

# Register your models here.
admin.site.register(VideoGame)
admin.site.register(UserProfile)
admin.site.register(Party)
