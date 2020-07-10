from django.contrib import admin
from django.urls import include, path, re_path
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
    api_detail_account_view,
    api_detail_all_accounts_view,
    api_update_account_view,
    api_delete_account_view,
    api_register_account_view,
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_screen_view, name="home"),
    path('register/', registation_view, name="register"),
    path('logout/', logout_view, name="logout"),
    path('login/', login_view, name="login"),
    path('account/', account_view, name="account"),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), name='password_change_done'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'), name='password_change'),
    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),

    path('osobe/', api_detail_all_accounts_view, name='osobe'),
    re_path(r'osobe/(?P<pk>\d+)', api_detail_account_view, name='osoba'),
    re_path(r'osobe/update/(?P<pk>\d+)', api_update_account_view, name='update'),
    re_path(r'osobe/delete/(?P<pk>\d+)', api_delete_account_view, name='delete'),
    re_path(r'osobe/register', api_register_account_view, name='create'),

]

