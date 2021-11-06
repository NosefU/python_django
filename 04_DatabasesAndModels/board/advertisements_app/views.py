from django.shortcuts import render
from django.views import generic

RUB_USD_EXCHANGE_RATE = 71.15

from advertisements_app.models import Advertisement


class AdvertisementsListView(generic.ListView):
    model = Advertisement
    context_object_name = 'advertisements'
    queryset = Advertisement.objects.all()[:10]


class AdvertisementsDetailView(generic.DetailView):
    model = Advertisement
    context_object_name = 'advertisement'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['usd_price'] = context['advertisement'].price / RUB_USD_EXCHANGE_RATE
        # TODO простейшая реализация, в дальнейшем можно будет кэшировать откуда-нибудь курс и тянуть его из кэша
        return context
