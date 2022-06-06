from django.urls import path
from phone_case import views

app_name = 'phone_case'

urlpatterns = [
    path('', views.CasesView.as_view(), name='lista_cases'),
    path('adaugare/', views.CreateCaseView.as_view(), name='adauga'),
    path('modificare/<int:pk>/', views.UpdateCaseView.as_view(), name='modifica'),
    path('sterge/<int:pk>/', views.deactivate_case, name='dezactiveaza'),
    path('buy/<int:pk>/', views.buycartView, name='buy'),
    path('successbuycase/<int:pk>/', views.updatequantityview, name='successbuycase'),
]
