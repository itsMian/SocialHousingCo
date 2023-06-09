# Generated by Django 4.2 on 2023-05-29 15:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Firstname', models.CharField(default='', max_length=100)),
                ('Lastname', models.CharField(default='', max_length=100)),
                ('DOB', models.DateField()),
                ('PhoneNum', models.CharField(default='', max_length=11)),
                ('aboutme', models.CharField(default='', max_length=2000)),
                ('User_id', models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('income_type', models.CharField(choices=[('salary', 'Salary'), ('family_allowance', 'Family Allowance'), ('child_support', 'Child Support')], default='salary', max_length=20)),
                ('pay_frequency', models.CharField(choices=[('annually', 'Annually'), ('monthly', 'Monthly'), ('fortnightly', 'Fortnightly'), ('weekly', 'Weekly')], default='annually', max_length=20)),
                ('amount_after_tax', models.DecimalField(decimal_places=2, max_digits=10)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Userprofile.profiles')),
            ],
        ),
    ]
