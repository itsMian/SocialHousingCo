# Generated by Django 4.2 on 2023-05-29 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0004_user_amount_after_tax_user_income_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='income_type',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='pay_frequency',
            field=models.CharField(default='', max_length=20),
        ),
    ]
