# Generated by Django 2.2.10 on 2022-03-02 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_auto_20220302_2008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lawyer',
            name='matricula',
            field=models.CharField(max_length=32, verbose_name='Matricula'),
        ),
    ]
