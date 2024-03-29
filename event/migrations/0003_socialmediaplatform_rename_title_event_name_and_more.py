# Generated by Django 5.0.3 on 2024-03-17 14:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_eventgenre_remove_event_created_by_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialMediaPlatform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('base_url', models.URLField()),
            ],
        ),
        migrations.RenameField(
            model_name='event',
            old_name='title',
            new_name='name',
        ),
        migrations.AddField(
            model_name='event',
            name='poster',
            field=models.ImageField(blank=True, null=True, upload_to='event_posters'),
        ),
        migrations.CreateModel(
            name='EventSocialMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.CharField(max_length=255)),
                ('hashtag', models.CharField(blank=True, max_length=255)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='social_media_accounts', to='event.event')),
                ('platform', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.socialmediaplatform')),
            ],
        ),
    ]
