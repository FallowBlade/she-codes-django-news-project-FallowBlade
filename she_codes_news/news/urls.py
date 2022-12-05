from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index')
]

# NOTE
# index is referring to our VIEWS
# Need a path for each question