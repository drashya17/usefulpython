# Generated by Django 2.0 on 2018-03-25 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0025_auto_20180325_1420'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='content_md',
            field=models.TextField(blank=True, null=True),
        ),
    ]
