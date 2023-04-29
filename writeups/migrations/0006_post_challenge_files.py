# Generated by Django 3.2.5 on 2023-04-29 22:21

from django.db import migrations
import writeups.formatChecker
import writeups.models


class Migration(migrations.Migration):

    dependencies = [
        ('writeups', '0005_auto_20230429_1423'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='challenge_files',
            field=writeups.formatChecker.SizeRestrictedFileField(blank=True, help_text="A compressed archive of this challenge's files. A 500MB limit is enforced.", null=True, upload_to=writeups.models.Post.make_challenge_filepath, verbose_name='Post files'),
        ),
    ]
