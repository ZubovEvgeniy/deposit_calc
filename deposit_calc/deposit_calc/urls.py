from django.urls import path

from calculator.views import DepositView


urlpatterns = [
    path('deposit', DepositView.as_view())
]
