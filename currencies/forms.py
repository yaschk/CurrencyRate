from django import forms
from .models import CurrencyRate
from django.forms.widgets import TextInput
from decimal import Decimal
from django.core.exceptions import ValidationError


class DateInput(forms.DateInput):
    """ Changes input type for date field """
    input_type = 'date'


class CurrencyRateForm(forms.Form):
    """ A form for creating currency rate for UAH to USD with date"""
    uah_rate = forms.CharField(label='UAH rate to 1 USD', required=True,
                                widget=TextInput(attrs={'placeholder': '0.00'}))
    date = forms.DateField(widget=DateInput(), required=True)

    class Meta:
        model = CurrencyRate
        fields = ('uah_rate', 'date')

    def clean_uah_rate(self):
        """ Validation function to allow users enter rate with ',' instead of '.' """
        data = self.cleaned_data['uah_rate']
        if ',' in data:
            data = data.replace(',', '.')
        try:
            data = float(data)
            if data <= 0:
                raise ValidationError("Should be a number greater than 0")
            Decimal.from_float(data)
        except ValueError:
            raise ValidationError("Should be a number")
        return data
