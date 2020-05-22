from .models import HttpRequestModel


class CustomMiddleware(object):
    def process_request(self, request):
        "collects requests and if not ajax saves it to DB"
        new_http_information = HttpRequestModel(
            path=request.path,
            method=request.method
            )
        if request.is_ajax():
            pass
        else:
            new_http_information.save()
