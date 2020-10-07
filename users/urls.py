from django.urls import path
from django_rest_passwordreset.views import reset_password_request_token, reset_password_confirm

from users.views import RegisterAccount, LoginAccount, AccountDetails, ConfirmAccount

app_name = 'users'
urlpatterns = [
    path('register', RegisterAccount.as_view(), name='user-register'),
    path('register/confirm', ConfirmAccount.as_view(), name='user-register-confirm'),
    path('details', AccountDetails.as_view(), name='user-details'),
    path('login', LoginAccount.as_view(), name='user-login'),
    path('password_reset', reset_password_request_token, name='password-reset'),
    path('password_reset/confirm', reset_password_confirm, name='password-reset-confirm'),
]
