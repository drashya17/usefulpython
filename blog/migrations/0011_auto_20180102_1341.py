# Generated by Django 2.0 on 2018-01-02 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20180102_1335'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='public_email',
            field=models.CharField(default='', max_length=40),
        ),
        migrations.AddField(
            model_name='profile',
            name='twitter_link',
            field=models.CharField(default='', max_length=30),
        ),
    ]
