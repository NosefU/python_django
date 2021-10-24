from django.http import HttpResponse

from django.views import View


class ToDoView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('<ul>'
                            '<li>Установить python</li>'
                            '<li>Установить django</li>'
                            '<li>Запустить сервер</li>'
                            '<li><b>Изменить список дел</b></li>'
                            '<li><b>Закоммитить и отправить на проверку</b></li>'
                            '</ul>')
