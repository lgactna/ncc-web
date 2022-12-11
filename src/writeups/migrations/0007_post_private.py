# Generated by Django 4.1.3 on 2022-12-11 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("writeups", "0006_alter_tag_name")]

    operations = [
        migrations.AddField(
            model_name="post",
            name="private",
            field=models.BooleanField(
                default=False,
                help_text="If true, this post requires the user be logged in to view.",
                verbose_name="Private post",
            ),
        )
    ]
