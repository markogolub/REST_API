from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from account.models import Account
from account.api.serializers import AccountSerializer, RegistrationSerializer


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

    if request.method == 'GET':
        data = []

        for account_values in accounts.values():
            del account_values['password']
            data.append(account_values)

        return Response({'osobe': data})


@api_view(('PUT',))
def api_update_account_view(request, pk, format=None):

    try:
        account = Account.objects.get(pk=pk)
    except Account.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = AccountSerializer(account, request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data["success"] = "Update successful."
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(('DELETE',))
def api_delete_account_view(request, pk, format=None):

    try:
        account = Account.objects.get(pk=pk)
    except Account.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        operation = account.delete()
        data = {}
        if operation:
            data["success"] = "Delete successful."
        else:
            data["failure"] = "Delete failed."
        return Response(data=data)


@api_view(('POST',))
def api_register_account_view(request):

    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = "Successfully registered a new user."
            data['email'] = account.email
            data['username'] = account.username
            data['name'] = account.name
            data['surname'] = account.surname
            data['phone'] = str(account.phone)
            data['cell_phone'] = str(account.cell_phone)
            data['address'] = account.address
            data['residence'] = account.residence
        else:
            data = serializer.errors
        print(data)
        return Response(data)