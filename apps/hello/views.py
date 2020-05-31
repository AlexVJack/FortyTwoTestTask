from django.views.generic import DetailView, ListView, UpdateView
from .tools import LoginRequiredMixin
from .models import HttpRequestModel, PersonInfo
from extra_views import ModelFormSetView


class PersonDetailView(DetailView):
    template_name = 'hello/personinfo.html'

    def get_object(self, queryset=None):
        return PersonInfo.objects.first()


class HttpRequestView(ListView):
    model = HttpRequestModel
    queryset = HttpRequestModel.objects.order_by('-priority', '-time')[:10]


class HttpRequestForms(ModelFormSetView):
    model = HttpRequestModel
    queryset = HttpRequestModel.objects.order_by('-priority', '-time')[:10]
    template_name = 'hello/edit_requests.html'


class PersonUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/'
    model = PersonInfo
    fields = ['name', 'last_name', 'date_of_bearth', 'bio', 'email',
              'jabber', 'skype', 'other_contacts']
