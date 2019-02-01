from django.shortcuts import render
from django.views.generic.detail import DetailView


class QuestionDetail(DetailView):

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        return ctx
