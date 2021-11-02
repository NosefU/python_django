from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

ADV_LIST = [
    'Nintendo Switch',
    'Nintendo Famicom',
    'Sony PlayStation',
    'Sega Dreamcast',
    'Sega Genesis',
    'Atari 26000',
    'Magnavox Odyssey',
]

post_requests = 0


class Advertisements(View):

    def get(self, request):
        return render(request, 'advertisements/advertisments.html', {'advertisments': ADV_LIST})

    def post(self, request):
        global post_requests
        post_requests += 1
        return HttpResponse(f'Объявление успешно добавлено на площадку<br>'
                            f'Добавлено объявлений: {post_requests}')


def advertisement_list(request, *args, **kwargs):
    advertisements = [
        'Мастер на час',
        'Выведение из запоя',
        'Услуги экскаватора-погрузчика, гидромолота, ямобура'
    ]
    advertisements_1 = [
        'Мастер на час',
        'Выведение из запоя',
        'Услуги экскаватора-погрузчика, гидромолота, ямобура'
    ]
    return render(request, 'advertisements/advertisement_list.html', {'advertisements': advertisements,
                                                                      'advertisements_1': advertisements_1})
