from django.shortcuts import render
from django.urls import reverse_lazy #from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView
from . import forms

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.sessions.backends.base import SessionBase


class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'
