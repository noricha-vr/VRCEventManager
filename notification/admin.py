from django.contrib import admin
from .models import TwitterAccount, DiscordWebhook, AnnouncementTemplate, EventAnnouncement

admin.site.register(TwitterAccount)
admin.site.register(DiscordWebhook)
admin.site.register(AnnouncementTemplate)
admin.site.register(EventAnnouncement)

