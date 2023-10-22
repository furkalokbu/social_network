from apps.posts.models import RequestHistory


class APIRequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if request.path.startswith("/api/v1/") and request.user.is_authenticated:
            log_entry = RequestHistory(
                method=request.method,
                path=request.path,
                user=request.user
            )
            log_entry.save()

        return response
