# Generated by Django 4.1.3 on 2022-12-05 05:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("writeups", "0002_alter_competition_content_alter_member_content_and_more")
    ]

    operations = [
        migrations.AddField(
            model_name="tag",
            name="theme_color",
            field=models.CharField(
                default="002E62",
                help_text="The background color used for this competition. Enter as 6 hex characters. Please make sure there's sufficient contrast!",
                max_length=6,
                validators=[
                    django.core.validators.RegexValidator(
                        "^[0-9a-fA-F]*$", "Only valid hex characters allowed."
                    ),
                    django.core.validators.MinLengthValidator(
                        6, message="Hex values must be exactly 6 in length."
                    ),
                ],
            ),
        )
    ]
