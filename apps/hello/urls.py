from django.conf.urls import url
from .views import HttpRequestView, PersonDetailView, PersonUpdateView
from .views import HttpRequestForms


urlpatterns = [
    url(r'^$', PersonDetailView.as_view(), name='main'),
    url(r'^requests/', HttpRequestView.as_view(), name='requests'),
    url(r'^update/(?P<pk>\d+)/$', PersonUpdateView.as_view(), name='update'),
    url(r'^updatereq/', HttpRequestForms.as_view(), name='updatereq')
]
