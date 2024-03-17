from django.db import models
from account.models import User
from event.models import Event

class TwitterAccount(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    consumer_key = models.CharField(max_length=255)
    consumer_secret = models.CharField(max_length=255)
    access_token = models.CharField(max_length=255)
    access_token_secret = models.CharField(max_length=255)

    def __str__(self):
        return f"Twitter Account for {self.event.name}"

class DiscordWebhook(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    webhook_url = models.URLField()

    def __str__(self):
        return f"Discord Webhook for {self.event.name}"

class AnnouncementTemplate(models.Model):
    name = models.CharField(max_length=255)
    twitter_template = models.JSONField(null=True, blank=True)
    discord_template = models.JSONField(null=True, blank=True)
    vrchat_template = models.JSONField(null=True, blank=True)

    def __str__(self):
        return self.name

class EventAnnouncement(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    template = models.ForeignKey(AnnouncementTemplate, on_delete=models.CASCADE)
    timing = models.DateTimeField()
    posted = models.BooleanField(default=False)

    def __str__(self):
        return f"Announcement for {self.event.name} using {self.template.name}"