from django.shortcuts import render, redirect
from .forms import CurrencyRateForm
from .models import CurrencyRate
import json
from django.db.models.query_utils import Q


def index(request):
    """ Index page view """

    # index form
    if request.method == 'POST':
        form = CurrencyRateForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data["date"]
            exists_rates = CurrencyRate.objects.filter(Q(date=date))
            if exists_rates:
                for rate in exists_rates:
                    obj = CurrencyRate.objects.get(date=date)
                    obj.uah_rate = form.cleaned_data["uah_rate"]
                    obj.save()
            else:
                obj = CurrencyRate()
                obj.uah_rate = form.cleaned_data["uah_rate"]
                obj.date = date
                obj.save()
            return redirect('index')
    else:
        form = CurrencyRateForm()

    # data for currency rate table
    q = CurrencyRate.objects.all().order_by('date')
    q_len = len(q)
    rates = [float(x.uah_rate) for x in q]
    dates = [str(x.date.strftime("%d-%m-%Y")) for x in q]

    return render(request, 'landing/index.html', {'form': form, 'rates': json.dumps(rates), 'dates': json.dumps(dates),
                                                  'rates_len': q_len})
