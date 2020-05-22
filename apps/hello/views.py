from django.views.generic import ListView
from .models import HttpRequestModel, PersonInfo


class PersonListView(ListView):
    model = PersonInfo


class HttpRequestView(ListView):
    model = HttpRequestModel
    queryset = HttpRequestModel.objects.order_by('-time')[:10]
