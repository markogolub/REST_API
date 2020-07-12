from account.models import Account
from django.shortcuts import render


def home_screen_view(request):
    context = {}

    accounts = Account.objects.all()
    context['accounts'] = accounts

    return render(request, "personal/home.html", context)