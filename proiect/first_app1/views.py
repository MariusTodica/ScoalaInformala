from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView

from first_app1.models import Companies


class CompanyView(LoginRequiredMixin, ListView):
    model = Companies
    template_name = 'first_app1/company_index.html'
    paginate_by = 5
    queryset = model.objects.filter(active=1)
    context_object_name = 'companies'

    def get_context_data(self, *args, **kwargs):
        data = super(CompanyView, self).get_context_data()
        # data['companies_list'] = self.model.objects.filter(active=1)
        return data


class CreateCompanyView(LoginRequiredMixin, CreateView):
    model = Companies
    fields = ['name', 'website', 'company_type', 'active']
    template_name = 'first_app1/company_form.html'

    def get_success_url(self):
        return reverse('companies:lista_companii')


class UpdateCompanyView(LoginRequiredMixin, UpdateView):
    model = Companies
    fields = ['name', 'website', 'company_type', 'active']
    template_name = 'first_app1/company_form.html'

    def get_success_url(self):
        return reverse('companies:lista_companii')


@login_required
def delete_company(request, pk):
    Companies.objects.filter(id=pk).update(active=0)
    return redirect('companies:lista_companii')


@login_required
def activate_company(request, pk):
    Companies.objects.filter(id=pk).update(active=1)
    return redirect('companies:lista_companii')


class CompanyInactiveView(LoginRequiredMixin, ListView):
    model = Companies
    template_name = 'first_app1/company_index.html'
    paginate_by = 5
    queryset = model.objects.filter(active=0)
    context_object_name = 'companies'

    def get_context_data(self, *args, **kwargs):
        data=super(CompanyInactiveView, self).get_context_data(*args, **kwargs)
        # data['companies_list'] = self.model.objects.filter(active=0)
        return data
