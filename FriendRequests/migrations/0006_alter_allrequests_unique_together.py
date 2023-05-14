# Generated by Django 4.1.5 on 2023-05-12 12:50

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('FriendRequests', '0005_rename_request_user_allrequests_request_id'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='allrequests',
            unique_together={('from_user', 'to_user')},
        ),
    ]
