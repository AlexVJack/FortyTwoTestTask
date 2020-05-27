from django.views.generic import DetailView, ListView, UpdateView
from .tools import LoginRequiredMixin
from .models import HttpRequestModel, PersonInfo


class PersonDetailView(DetailView):
    template_name = 'hello/personinfo.html'

    def get_object(self, queryset=None):
        return PersonInfo.objects.first()


class HttpRequestView(ListView):
    model = HttpRequestModel
    queryset = HttpRequestModel.objects.order_by('-time')[:10]


class PersonUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/'
    model = PersonInfo
    fields = ['name', 'last_name', 'date_of_bearth', 'bio', 'email',
              'jabber', 'skype', 'other_contacts']
