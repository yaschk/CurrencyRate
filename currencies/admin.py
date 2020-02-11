from django.contrib import admin
from .models import CurrencyRate


class CurrencyRateAdmin (admin.ModelAdmin):
    list_display = [field.name for field in CurrencyRate._meta.fields]

    class Meta:
        model = CurrencyRate


admin.site.register(CurrencyRate, CurrencyRateAdmin)

