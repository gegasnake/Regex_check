from django.views.generic import TemplateView
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from .forms import RegexCheckForm
from django.views import View
import re


class RegexFormView(View):
    form_class = RegexCheckForm
    initial = {'key': 'value'}
    template_name = 'regex_main_app/regex_form.html'

    def get(self, request):
        form = RegexCheckForm()
        return render(request, 'regex_main_app/regex_form.html', {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            data = form.cleaned_data['text']
            pattern = form.cleaned_data['pattern']
            if re.match(pattern, data):
                return HttpResponseRedirect('matches/')
            else:
                return HttpResponseRedirect('doesnotmatch/')

        return render(request, 'regex_main_app/regex_form.html', {"form": form})


class RegexMatchesView(TemplateView):
    template_name = 'regex_main_app/matches.html'



class RegexDoesNotMatchView(TemplateView):
    template_name = 'regex_main_app/doesnotmatch.html'


