from django.shortcuts import render

CONTEXTS = {
    'python': {
        'title': 'Профессия Python-разработчик',
        'img_url': 'https://248006.selcdn.ru/LandGen/phone_4589beaf332198133164e04e0fb855c2c1368858.webp',
        'course_url': 'https://skillbox.ru/course/profession-python/',
        'price': 1000,
        'bg_colour': '#60B3FF'
    },
    '1c': {
        'title': 'Профессия 1С-разработчик',
        'img_url': 'https://248006.selcdn.ru/LandGen/desktop_468cebf77a00674e98b6e8322a7caf3a31761433.webp',
        'course_url': 'https://skillbox.ru/course/profession-1c/',
        'price': 2000,
        'bg_colour': '#FFD773'
    },
    'web': {
        'title': 'Профессия Веб-разработчик',
        'img_url': 'https://248006.selcdn.ru/LandGen/desktop_1483b955a743f9098806cbe6c6d78d306a210b65.webp',
        'course_url': 'https://skillbox.ru/course/profession-webdev/',
        'price': 800,
        'bg_colour': '#A3A3FF'
    },
    'java': {
        'title': 'Профессия Java-разработчик',
        'img_url': 'https://248006.selcdn.ru/LandGen/desktop_477ae814606ca5e5256c683921f40d2d7f29bad4.webp',
        'course_url': 'https://skillbox.ru/course/profession-java/',
        'price': 1300,
        'bg_colour': '#FFBD59'
    },
    'android': {
        'title': 'Профессия Android-разработчик',
        'img_url': 'https://248006.selcdn.ru/LandGen/desktop_763111395fcf224a8e694cdfbf3bb3d198914536.webp',
        'course_url': 'https://skillbox.ru/course/profession-android-developer-2021/',
        'price': 1500,
        'bg_colour': '#FFC27F'
    },
}


def adv_list(request, *args, **kwargs):
    return render(request, 'advertisement/adv_list.html', {})


def adv_details(request, *args, **kwargs):
    course = request.GET.get('adv')
    if not course:
        return render(request, 'advertisement/404.html')
    return render(request, 'advertisement/adv_details.html', CONTEXTS[course])
