# Generated by Django 4.2.14 on 2024-07-23 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0004_event"),
    ]

    operations = [
        migrations.AddField(
            model_name="event",
            name="location",
            field=models.CharField(default="TBD", max_length=255),
            preserve_default=False,
        ),
    ]