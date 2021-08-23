from django.contrib import admin
from .models import VideoGame, UserProfile, Party, PartyMessage

# Register your models here.
admin.site.register(VideoGame)
admin.site.register(UserProfile)
admin.site.register(Party)
admin.site.register(PartyMessage)
