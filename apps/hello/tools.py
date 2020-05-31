from django.contrib.auth.decorators import login_required
from django.utils import simplejson
from django.http import HttpResponse


class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)


class JsonResponse(HttpResponse):
    """
        JSON response
    """
    def __init__(self, content, mimetype='application/json',
                 status=None, content_type=None):
        super(JsonResponse, self).__init__(
            content=simplejson.dumps(content),
            mimetype=mimetype,
            status=status,
            content_type=content_type,
        )
