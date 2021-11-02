from datetime import datetime


class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        line = datetime.now().isoformat(timespec='milliseconds')
        line += ' ' + request.path
        line += ' ' + request.META.get('REQUEST_METHOD')
        with open('requests.log', 'a', encoding='utf8') as f:
            print(line, file=f)
        response = self.get_response(request)
        return response
