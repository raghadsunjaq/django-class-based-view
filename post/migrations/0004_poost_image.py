# Generated by Django 3.1.4 on 2020-12-12 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_poost_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='poost',
            name='image',
            field=models.ImageField(default=None, upload_to='post/'),
        ),
    ]
