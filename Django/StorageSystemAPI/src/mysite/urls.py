from django.contrib import admin
from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from personal.views import (
    home_screen_view
)
from account.views import (
    registation_view,
    logout_view,
    login_view,
    account_view,
)
from account.api.views import (
    api_create_location,
    api_detail_account_view,
    api_detail_all_accounts_view,
    api_delete_account_view,
    api_register_account_view,
    api_show_all_locations,
    api_update_account_view,
    UserListView,
    LoginAuthTokenView,
)
urlpatterns = [
    path('', home_screen_view, name="home"),
    path('account/', account_view, name="account"),
    path('admin/', admin.site.urls),
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name="logout"),
    path('password_change/', auth_views.PasswordChangeView.as_view(
        template_name='registration/password_change.html'),
         name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='registration/password_change_done.html'),
         name='password_change_done'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='registration/password_reset_done.html'),
         name='password_reset_done'),
    path('register/', registation_view, name="register"),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='registration/password_reset_complete.html'),
         name='password_reset_complete'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),

    # REST API URLS
    path('osobe/', api_detail_all_accounts_view, name='osobe'),
    path('osobe/login', LoginAuthTokenView.as_view(), name="api_login"),
    path('osobe/location/search/', UserListView.as_view()),
    path('osobe/register', api_register_account_view, name='api_create'),
    re_path(r'osobe/delete/(?P<pk>\d+)', api_delete_account_view, name='api_delete'),
    re_path(r'osobe/location/create/(?P<pk>\d+)', api_create_location, name='api_location'),
    re_path(r'osobe/locations/(?P<pk>\d+)', api_show_all_locations, name='api_all_locations'),
    re_path(r'osobe/update/(?P<pk>\d+)', api_update_account_view, name='api_update'),
    re_path(r'osobe/(?P<pk>\d+)', api_detail_account_view, name='osoba'),
]


