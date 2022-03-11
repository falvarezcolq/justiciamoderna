# Generated by Django 2.2.10 on 2022-03-10 19:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0019_remove_area_lawyers'),
    ]

    operations = [
        migrations.CreateModel(
            name='LawyerArea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='modified at')),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Area')),
                ('lawyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Lawyer')),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='area',
            name='lawyers',
            field=models.ManyToManyField(through='users.LawyerArea', to='users.Lawyer'),
        ),
    ]
