# Generated by Django 4.2.1 on 2023-05-09 22:32

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('FriendRequests', '0002_rename_friendrequests_frndrequests'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FrndRequests',
            new_name='AllRequests',
        ),
    ]
