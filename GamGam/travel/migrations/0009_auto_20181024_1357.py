# Generated by Django 2.1.2 on 2018-10-24 13:57

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0008_auto_20181023_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travel',
            name='main_image',
            field=imagekit.models.fields.ProcessedImageField(upload_to='uploads/%Y/%m/%d/'),
        ),
    ]