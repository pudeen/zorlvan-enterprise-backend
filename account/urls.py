from django.urls import path
from account.views import(
    registration_view,
    LoginView,
    account_profile_view
)
from rest_framework.authtoken.views import obtain_auth_token

app_name = 'account'

urlpatterns = [
    path('register', registration_view),
    path('login', LoginView.as_view()), 
    path('profile', account_profile_view)
]