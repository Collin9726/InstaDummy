# Generated by Django 3.0.8 on 2020-07-04 12:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instaapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comment_text',
            new_name='comment',
        ),
        migrations.RenameField(
            model_name='image',
            old_name='name',
            new_name='image_name',
        ),
        migrations.RenameField(
            model_name='image',
            old_name='url',
            new_name='image_upload',
        ),
    ]