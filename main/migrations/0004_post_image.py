# Generated by Django 3.1.6 on 2021-03-10 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210302_1910'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to='post_pics', verbose_name='Image'),
        ),
    ]
