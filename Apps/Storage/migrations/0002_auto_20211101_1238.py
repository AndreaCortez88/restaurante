# Generated by Django 2.0.6 on 2021-11-01 18:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Storage', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='extras',
            old_name='imagen1',
            new_name='imagen1_ext',
        ),
        migrations.RenameField(
            model_name='postres',
            old_name='imagen1',
            new_name='imagen1_post',
        ),
    ]