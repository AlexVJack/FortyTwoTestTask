from django.views.generic import ListView
from .models import PersonInfo


class PersonListView(ListView):
    model = PersonInfo
