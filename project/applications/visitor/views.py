import json
from django.http import JsonResponse, HttpResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.views.generic.detail import BaseDetailView
from .forms import RegisterForm
from .models import VisitorContext, VisitorManager


class RegisterFormView(View):
    form_class = RegisterForm
    template_name = 'visitor/register-form.html'

    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            manager= VisitorManager()

            date_of_birth = manager.merge_separated_date_of_birth(
                request.POST.get('date_of_birth_year', None),
                request.POST.get('date_of_birth_month', None),
                request.POST.get('date_of_birth_day', None),
            )
            visitor_context = VisitorContext(
                request.POST.get('mobile_number', None),
                request.POST.get('email', None),
                request.POST.get('first_name', None),
                request.POST.get('last_name', None),
                date_of_birth,
                request.POST.get('gender', None)
            )
            manager.create_new_visitor(visitor_context)

        return HttpResponse(json.dumps({'name': 'syarief'}), content_type="application/json")


class LoginView(TemplateView):
    template_name = 'visitor/login-form.html'
