# Generated by Django 4.1.3 on 2022-12-14 18:28

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):
    dependencies = [("writeups", "0001_initial")]

    operations = [
        migrations.AddField(
            model_name="member",
            name="profile_image",
            field=models.ImageField(blank=True, null=True, upload_to="profiles"),
        ),
        migrations.AddField(
            model_name="post",
            name="meta_image",
            field=models.ImageField(blank=True, null=True, upload_to="post-banners"),
        ),
        migrations.AddField(
            model_name="tag",
            name="content",
            field=tinymce.models.HTMLField(
                default="",
                help_text="A TinyMCE-driven field for the tag's page content.",
                verbose_name="Page content",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="tool",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="tool-images"),
        ),
    ]
