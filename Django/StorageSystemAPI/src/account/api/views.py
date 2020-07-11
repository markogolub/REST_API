from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from account.models import Account, Location
from account.api.serializers import AccountSerializer, RegistrationSerializer


@api_view(('GET',))
@permission_classes((IsAuthenticated,))
def api_detail_account_view(request, pk, format=None):

    try:
        account = Account.objects.get(pk=pk)
    except Account.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AccountSerializer(account)
        return Response(serializer.data)


@api_view(('GET',))
@permission_classes((IsAuthenticated,))
def api_detail_all_accounts_view(request):

    try:
        accounts = Account.objects.all()
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if not request.user.is_superuser:
        return Response({'response': "You don't have permission to see this informations."})

    if request.method == 'GET':
        data = []

        for account_values in accounts.values():
            del account_values['password']
            data.append(account_values)

        return Response({'osobe': data})


@api_view(('PUT',))
@permission_classes((IsAuthenticated,))
def api_update_account_view(request, pk, format=None):

    try:
        account = Account.objects.get(pk=pk)
    except Account.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    user = request.user
    if account != user:
        return Response({'response': "You don't have permission to update this informations."})

    if request.method == 'PUT':
        serializer = AccountSerializer(account, request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data["success"] = "Update successful."
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(('DELETE',))
@permission_classes((IsAuthenticated,))
def api_delete_account_view(request, pk, format=None):

    try:
        account = Account.objects.get(pk=pk)
    except Account.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    user = request.user
    if account != user:
        return Response({'response': "You don't have permission to delete this informations."})

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
            token = Token.objects.get(user=account).key
            data['token'] = token
        else:
            data = serializer.errors
        print(data)
        return Response(data)


@api_view(('GET',))
@permission_classes((IsAuthenticated,))
def api_show_all_locations(request, pk, format=None):

    try:
        account = Account.objects.get(pk=pk)
    except Account.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    user = request.user
    if account != user:
        return Response({'response': "You don't have permission to see this informations."})

    if request.method == 'GET':
        data = {}
        locations_list = []

        locations = list(account.location_set.all())
        for location in locations:
            locations_list.append({'latitude': float(location.latitude),
                                   'longitude': float(location.longitude),
                                   'time': str(location.time)})

        data['locations'] = locations_list
        if data['locations']:
            return Response(data=data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(('POST',))
@permission_classes((IsAuthenticated,))
def api_create_location(request, pk, format=None):

    try:
        account = Account.objects.get(pk=pk)
    except Account.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    user = request.user
    if account != user:
        return Response({'response': "You don't have permission to add this information."})

    if request.method == 'POST':
        data = {}

        try:
            new_location = Location(latitude=request.data['latitude'], longitude=request.data['longitude'], account=account)
            new_location.save()

            data['succes'] = "Created new location."

            return Response(data)
        except:
            return Response(data, status=status.HTTP_400_BAD_REQUEST)