from django.shortcuts import render
from django.views.generic.detail import DetailView

from .models import Question


class QuestionDetail(DetailView):
    model = Question

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        return ctx
