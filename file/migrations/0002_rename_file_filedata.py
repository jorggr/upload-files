# Generated by Django 5.0.2 on 2024-03-01 18:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("file", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="File",
            new_name="FileData",
        ),
    ]
