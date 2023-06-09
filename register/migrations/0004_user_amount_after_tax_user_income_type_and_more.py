# Generated by Django 4.2 on 2023-05-29 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0003_user_aboutme'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='amount_after_tax',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='user',
            name='income_type',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='user',
            name='pay_frequency',
            field=models.CharField(default='', max_length=20),
        ),
    ]
