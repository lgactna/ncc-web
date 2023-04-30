# Generated by Django 3.2.5 on 2023-04-30 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('writeups', '0006_post_challenge_files'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='private',
            field=models.BooleanField(default=True, help_text='If a post is set to private, users must be logged in to view the post. Linking to the post will also hide its meta details.', verbose_name='Private?'),
            preserve_default=False,
        ),
    ]