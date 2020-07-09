from django.shortcuts import render
from account.models import Account

def home_screen_view(request):
    contex = {}

    accounts = Account.objects.all()
    contex['accounts'] = accounts

    return render(request, "personal/home.html", {})