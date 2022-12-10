from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.StoryView.as_view(), name='story'),
    path ('add-story/', views.AddStoryView.as_view(), name='newStory')
]

# NOTE
# index is referring to our VIEWS
# Need a path for each question