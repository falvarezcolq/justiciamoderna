# Generated by Django 2.2.10 on 2022-02-13 20:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rols', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rolpermission',
            old_name='states',
            new_name='state',
        ),
    ]
