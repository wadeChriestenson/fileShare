# Generated by Django 4.0.4 on 2022-04-24 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('standard', '0004_userfiles_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='userfiles',
            name='userName',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
