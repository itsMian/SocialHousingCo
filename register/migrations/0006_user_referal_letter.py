# Generated by Django 4.2 on 2023-05-30 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0005_user_photoid_user_secondid'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='referal_letter',
            field=models.FileField(blank=True, upload_to='media/'),
        ),
    ]
