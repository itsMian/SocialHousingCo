from django.db import models

class Profiles(models.Model):
    Firstname = models.CharField(max_length=100,default='')
    Lastname = models.CharField(max_length=100,default='')
    DOB = models.DateField()
    PhoneNum = models.CharField(max_length=11,default='')
    aboutme = models.CharField(max_length=2000,default='')

class Income(models.Model):
    profile = models.ForeignKey(Profiles, on_delete=models.CASCADE)
    INCOME_TYPE_CHOICES = [
        ('salary', 'Salary'),
        ('family_allowance', 'Family Allowance'),
        ('child_support', 'Child Support'),
    ]

    PAY_FREQUENCY_CHOICES = [
        ('annually', 'Annually'),
        ('monthly', 'Monthly'),
        ('fortnightly', 'Fortnightly'),
        ('weekly', 'Weekly'),
    ]

    income_type = models.CharField(max_length=20, choices=INCOME_TYPE_CHOICES, default='salary')
    pay_frequency = models.CharField(max_length=20, choices=PAY_FREQUENCY_CHOICES, default='annually')
    amount_after_tax = models.DecimalField(max_digits=10, decimal_places=2)
