from django.shortcuts import render
from myapp.models import DemoModel
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


class DemoListView(ListView):
    model = DemoModel


class DemoDetailView(DetailView):
    model = DemoModel