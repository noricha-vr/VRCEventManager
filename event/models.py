from account.models import User

from django.db import models

class EventGenre(models.Model):
    EVENT_CALENDER_GENRE_CHOICES = (
        ('avatar_fitting', 'アバター試着会'),
        ('avatar_modification', '改変アバター交流会'),
        ('other_social', 'その他交流会'),
        ('vr_drinking', 'VR飲み会'),
        ('store_event', '店舗系イベント'),
        ('music_event', '音楽系イベント'),
        ('academic_event', '学術系イベント'),
        ('role_playing', 'ロールプレイ'),
        ('beginner_event', '初心者向けイベント'),
        ('regular_event', '定期イベント'),
    )

    name = models.CharField(max_length=255)
    event_calender_genre = models.CharField(max_length=255, choices=EVENT_CALENDER_GENRE_CHOICES, null=True, blank=True)

    def __str__(self):
        return self.name

class Event(models.Model):
    PLATFORM_CHOICES = (
        ('pc', 'PCオンリー'),
        ('pc_android', 'PC/Android両対応（Android対応）'),
        ('android', 'Android オンリー'),
    )

    name = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    group_id = models.CharField(max_length=8,default=None, null=True, blank=True)
    platform_compatibility = models.CharField(max_length=20, choices=PLATFORM_CHOICES, default='pc')
    genres = models.JSONField(default=list, blank=True)
    poster = models.ImageField(upload_to='event_posters', null=True, blank=True)

    def __str__(self):
        return self.name

class SocialMediaPlatform(models.Model):
    name = models.CharField(max_length=255)
    base_url = models.URLField()

    def __str__(self):
        return self.name

class EventSocialMedia(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='social_media_accounts')
    platform = models.ForeignKey(SocialMediaPlatform, on_delete=models.CASCADE)
    account = models.CharField(max_length=255)
    hashtag = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.event.name} - {self.platform.name}"

class RecurrenceRule(models.Model):
    FREQUENCY_CHOICES = (
        ('NONE', '設定なし'),
        ('CUSTOM', 'カスタム'),
        ('DAILY', '毎日'),
        ('WEEKLY', '毎週'),
        ('BIWEEKLY', '隔週'),
        ('MONTHLY', '毎月'),
        ('YEARLY', '毎年'),
    )

    WEEKDAY_CHOICES = (
        (0, '月曜日'),
        (1, '火曜日'),
        (2, '水曜日'),
        (3, '木曜日'),
        (4, '金曜日'),
        (5, '土曜日'),
        (6, '日曜日'),
    )

    OCCURRENCE_CHOICES = (
        (1, '第1'),
        (2, '第2'),
        (3, '第3'),
        (4, '第4'),
        (-1, '最終'),
    )

    event = models.OneToOneField(Event, on_delete=models.CASCADE, related_name='recurrence_rule')
    frequency = models.CharField(max_length=10, choices=FREQUENCY_CHOICES, default='NONE')
    interval = models.PositiveIntegerField(default=1)
    weekdays = models.JSONField(null=True, blank=True)
    month_day = models.IntegerField(null=True, blank=True)
    month = models.IntegerField(null=True, blank=True)
    occurrence = models.IntegerField(choices=OCCURRENCE_CHOICES, null=True, blank=True)
    weekday = models.IntegerField(choices=WEEKDAY_CHOICES, null=True, blank=True)
    custom_dates = models.JSONField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.event.name} - {self.frequency} Recurrence Rule"


class EventInstance(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    is_deleted = models.BooleanField(default=False)



class EventRole(models.Model):
    EVENT_ROLE_CHOICES = (
        ('organizer', '主催者'),
        ('staff', 'スタッフ'),
    )
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=EVENT_ROLE_CHOICES)

    class Meta:
        unique_together = ('event', 'user')