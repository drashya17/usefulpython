# Generated by Django 2.0 on 2017-12-31 03:12

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20171231_0633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='content',
            field=tinymce.models.HTMLField(null=True),
        ),
    ]