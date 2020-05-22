from django.conf.urls import url
from .views import HttpRequestView, PersonListView


urlpatterns = [
    url(r'^$', PersonListView.as_view(), name='main'),
    url(r'^requests/', HttpRequestView.as_view(), name='requests'),
]
