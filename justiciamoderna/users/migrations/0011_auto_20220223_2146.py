# Generated by Django 2.2.10 on 2022-02-23 21:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_degree'),
    ]

    operations = [
        migrations.AddField(
            model_name='degree',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, help_text='Date time on which the object was created.', verbose_name='created at'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='degree',
            name='img_l',
            field=models.FileField(max_length=255, null=True, upload_to='x/x1', verbose_name='picture size large 1024x1024'),
        ),
        migrations.AddField(
            model_name='degree',
            name='img_m',
            field=models.FileField(default='', max_length=255, null=True, upload_to='x/x5', verbose_name='picture size medium 400x400'),
        ),
        migrations.AddField(
            model_name='degree',
            name='modified',
            field=models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='modified at'),
        ),
        migrations.AddField(
            model_name='degree',
            name='thumbnail',
            field=models.FileField(default='', max_length=255, null=True, upload_to='x/x4', verbose_name='picture size small 70x70'),
        ),
    ]
