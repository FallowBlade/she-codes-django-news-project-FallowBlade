from django.urls import path
from .views import CreateAccountView, AccountProfileView, EditAccountView


app_name = 'users'

urlpatterns = [
    path('create-account/', CreateAccountView.as_view(), name='createAccount'),
    path('<int:pk>', AccountProfileView.as_view(), name='AccountProfile'),
    path('<int:pk>/edit', EditAccountView.as_view(), name='EditProfile'),
]

# int pk references a uniqueue user ID
