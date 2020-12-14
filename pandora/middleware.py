from pandora import box


class RequestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        box['request'] = request

        response = self.get_response(request)

        return response


class UserMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        box['user'] = request.user

        response = self.get_response(request)

        return response
