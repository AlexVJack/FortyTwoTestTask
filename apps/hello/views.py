from django.views.generic import ListView, UpdateView
from .tools import LoginRequiredMixin
from .models import HttpRequestModel, PersonInfo


class PersonListView(ListView):
    model = PersonInfo


class HttpRequestView(ListView):
    model = HttpRequestModel
    queryset = HttpRequestModel.objects.order_by('-time')[:10]


class PersonUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/'
    model = PersonInfo
    fields = ['name', 'last_name', 'date_of_bearth', 'bio', 'email',
              'jabber', 'skype', 'other_contacts']
