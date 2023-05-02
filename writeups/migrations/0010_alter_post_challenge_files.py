# Generated by Django 3.2.5 on 2023-05-02 02:29

from django.db import migrations
import writeups.formatChecker
import writeups.models


class Migration(migrations.Migration):

    dependencies = [
        ('writeups', '0009_auto_20230430_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='challenge_files',
            field=writeups.formatChecker.SizeRestrictedFileField(blank=True, help_text="A compressed archive of this challenge's files. A 100MB limit is enforced.", null=True, upload_to=writeups.models.Post.make_challenge_filepath, verbose_name='Post files'),
        ),
    ]
