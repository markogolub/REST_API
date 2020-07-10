from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from account.models import Account
from account.api.serializers import AccountSerializer


@api_view(('GET',))
def api_detail_account_view(request, pk, format=None):

    try:
        account = Account.objects.get(pk=pk)
    except Account.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AccountSerializer(account)
        return Response(serializer.data)


@api_view(('GET',))
def api_detail_all_accounts_view(request):

    try:
        accounts = Account.objects.all()
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    data = []

    for account_values in accounts.values():
        del account_values['password']
        data.append(account_values)


    return Response({'osobe': data})