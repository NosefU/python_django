import random
from typing import List

from django.http import HttpResponse

from django.views import View


def get_tasks(count: int = 5) -> List[str]:
    tasks = [
        'PSP: buy new housing shell',
        'Wii: replace broken USB ports',
        'Famicom: retrobright housing shell',
        'Dreamcast: buy new gamepad',
        'PS2: Buy network adapter',
        'PS1: Buy PSIO',
        'X360: buy wide angle lens for kinect',
        'PSP: buy microsd to memory stick duo adapter',
        'Famicom: buy CoolGirl',
        'PVM: replace resistor on sync channer',
    ]
    if len(tasks) < count:
        count = len(tasks)
    return random.sample(tasks, count)


class ToDoView(View):

    def get(self, request, *args, **kwargs):
        content = '<ul>'
        for task in get_tasks(5):
            content += f'<li>{task}</li>'
        content += '</ul>'
        return HttpResponse(content)
