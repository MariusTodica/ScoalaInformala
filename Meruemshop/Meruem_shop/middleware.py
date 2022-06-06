
from phone_case.models import Logs_Cases


class RefreshMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            print(request.method)
            if request.method == 'GET':
                Logs_Cases.objects.create(user_id=request.user.id, action='refresh', url=request.path)
            elif request.method == 'POST':
                action = 'created'
                for item in str(request.path):
                    if item.isdigit():
                        action = 'updated'
                        break
                Logs_Cases.objects.create(user_id=request.user.id, action=action, url=request.path)
        response = self.get_response(request)
        return response
