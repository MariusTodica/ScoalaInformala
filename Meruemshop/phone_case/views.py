from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import CreateView, ListView, UpdateView
from phone_case.models import Case
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from phone_case.forms import BuyForm

class CreateCaseView(LoginRequiredMixin, CreateView):
    model = Case
    fields = ['name', 'material', 'color', 'image', 'price', 'stock']
    template_name = 'phone_case_form.html'

    def get_success_url(self):
        return reverse('phone_case:adauga')


class CasesView(ListView):
    model = Case
    template_name = 'phone_case_index.html'
    paginate_by = 5

    def get_queryset(self):
        return Case.objects.filter(active=True)


class UpdateCaseView(UpdateView):
    model = Case
    fields = ['price', 'stock']
    template_name = 'phone_case_form.html'

    def get_queryset(self):
        return Case.objects.filter(active=True)

    def get_success_url(self):
        return reverse('phone_case:lista_cases')


@login_required
def deactivate_case(request, pk):
    if Case.objects.filter(id=pk).exists:
        Case.objects.filter(id=pk).update(active=False)
    return redirect('phone_case:lista_cases')


def buycartView(request, pk):
    if Case.objects.filter(id=pk).exists():
        if request.method == 'GET':
            form = BuyForm()
        else:
            form = BuyForm(request.POST)
            if form.is_valid():
                first_name = form.cleaned_data['first_name']
                last_name = form.cleaned_data['last_name']
                email = form.cleaned_data['email']
                address = form.cleaned_data['address']
                try:
                    send_mail(first_name, last_name, email, ['admin@example.com'], address)
                except BadHeaderError:
                    return HttpResponse('Invalid header found.')
                return render(request, 'successbuy.html')
        return render(request, "buycarts.html", {'form': form})


# def successbuyView(request):
#     return HttpResponse('Success! Thank you for your message.')


def updatequantityview(request, pk):
    if Case.objects.filter(id=pk).exists():
        case_instance = Case.objects.get(id=pk)
        case = case_instance.quantity
        if case > 0:
            Case.objects.filter(id=case_instance.id).update(stock=case-1)
        else:
            pass
    return redirect('phone_case:lista_cases')


# @login_required()
# def updatestockview(request, pk):
#     if Case.objects.filter(id=pk).exists():
#         case_instance = Case.objects.get(id=pk)
#         case = case_instance.stock
#         if case > 0:
#             Case.objects.filter(id=case_instance.id).update(stock=case-1)
#         else:
#             pass
#     return redirect('phone_case:lista_cases')
