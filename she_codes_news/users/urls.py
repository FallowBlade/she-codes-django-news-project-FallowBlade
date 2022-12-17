from django.urls import path
from .views import CreateAccountView, AccountProfileView


app_name = 'users'

urlpatterns = [
    path('create-account/', CreateAccountView.as_view(), name='createAccount'),
    path('<int:pk>', AccountProfileView.as_view(), name='AccountProfile'),
]

# int pk references a uniqueue user ID
