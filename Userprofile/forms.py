from django import forms
from .models import Income

class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ['income_type', 'pay_frequency', 'amount_after_tax']
