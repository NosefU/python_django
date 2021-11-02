from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

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


class Contacts(TemplateView):
    template_name = 'advertisements/contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'address': 'City, Street 1, office 1',
            'phone': '+7 999 999-99-99',
            'email': 'mail@mail.com'
        })
        return context


class About(TemplateView):
    template_name = 'advertisements/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'company_name': 'ООО «Вектор»',
            'description': """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod 
            tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud 
            exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor 
            in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur 
            sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est 
            laborum."""
        })
        return context

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
