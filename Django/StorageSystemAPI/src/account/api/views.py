from account.models import Account, Location
from account.api.serializers import AccountSerializer, RegistrationSerializer
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response


@api_view(('GET',))
@permission_classes((IsAuthenticated,))
def api_detail_account_view(request, pk, format=None):

    try:
        account = Account.objects.get(pk=pk)
    except Account.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    user = request.user
    if not user.is_superuser and user.pk != account.pk:
        return Response({'response': "You don't have permission to see this informations."})

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
        account_details = []

        for account_values in accounts.values():
            del account_values['password']
            account_details.append(account_values)

        return Response({'osobe': account_details})


@api_view(('PUT',))
@permission_classes((IsAuthenticated,))
def api_update_account_view(request, pk, format=None):

    try:
        account = Account.objects.get(pk=pk)
    except Account.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    user = request.user
    if not user.is_superuser and account != user:
        return Response({'response': "You don't have permission to update this informations."})

    if request.method == 'PUT':
        context = {}
        serializer = AccountSerializer(account, request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            context["success"] = "Update successful."
            return Response(data=context)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(('DELETE',))
@permission_classes((IsAuthenticated,))
def api_delete_account_view(request, pk, format=None):

    try:
        account = Account.objects.get(pk=pk)
    except Account.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    user = request.user
    if not user.is_superuser and account != user:
        return Response({'response': "You don't have permission to delete this informations."})

    if request.method == 'DELETE':
        context = {}
        operation = account.delete()

        if operation:
            context["success"] = "Delete successful."
        else:
            context["failure"] = "Delete failed."

        return Response(data=context)


@api_view(('POST',))
@permission_classes(())
def api_register_account_view(request):

    if request.method == 'POST':
        context = {}
        serializer = RegistrationSerializer(data=request.data)

        if serializer.is_valid():
            account = serializer.save()
            token = Token.objects.get(user=account)
            context['response'] = "Successfully registered a new user."
            context['email'] = account.email
            context['username'] = account.username
            context['name'] = account.name
            context['surname'] = account.surname
            context['phone'] = str(account.phone)
            context['cell_phone'] = str(account.cell_phone)
            context['address'] = account.address
            context['residence'] = account.residence
            context['date_joined'] = account.date_joined
            context['token'] = token.key
            return Response(data=context)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(('GET',))
@permission_classes((IsAuthenticated,))
def api_show_all_locations(request, pk, format=None):

    try:
        account = Account.objects.get(pk=pk)
    except Account.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    user = request.user
    if not user.is_superuser and account != user:
        return Response({'response': "You don't have permission to see this informations."})

    if request.method == 'GET':
        context = {}
        locations_list = []
        locations = list(account.location_set.all())

        for location in locations:
            locations_list.append({'latitude': float(location.latitude),
                                   'longitude': float(location.longitude),
                                   'time': str(location.time)})

        context['locations'] = locations_list

        if context['locations']:
            return Response(data=context)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


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
        context = {}

        try:
            new_location = Location(latitude=request.data['latitude'], longitude=request.data['longitude'], account=account)
            new_location.save()
            context['success'] = "Created new location."
            return Response(data=context)

        except:
            return Response(data=context, status=status.HTTP_400_BAD_REQUEST)


class UserListView(ListAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('address', )


class LoginAuthTokenView(APIView):

    authentication_classes = []
    permission_classes = []

    def post(self, request):
        context = {}

        # Django default. First field must be 'username' even when logging in with email.
        email = request.POST.get('username')
        password = request.POST.get('password')
        account = authenticate(email=email, password=password)
        if account:
            try:
                token = Token.objects.get(user=account)
            except Token.DoesNotExist:
                token = Token.objects.create(user=account)
            context['response'] = "Successfully authenticated."
            context['pk'] = account.pk
            context['token'] = token.key
        else:
            context['response'] = "Error!"
            context['error_message'] = "Invalid credentials."

        return Response(data=context)