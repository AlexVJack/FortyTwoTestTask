from django.conf.urls import url
from .views import PersonListView


urlpatterns = [
    url(r'^$', PersonListView.as_view(), name='main'),
]
