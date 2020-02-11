from django.db import models


class CurrencyRate(models.Model):
    """ A model for currency rate item"""
    uah_rate = models.fields.DecimalField(blank=False, null=False, max_digits=6, decimal_places=2)
    date = models.fields.DateField(blank=False, null=False, unique=True, db_index=True)
    is_created = models.DateTimeField(auto_now_add=True, auto_now=False)
    is_updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return '%s ' % self.date
