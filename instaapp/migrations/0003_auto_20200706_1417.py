# Generated by Django 3.0.8 on 2020-07-06 11:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instaapp', '0002_auto_20200706_1354'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comment',
            new_name='your_comment',
        ),
    ]
