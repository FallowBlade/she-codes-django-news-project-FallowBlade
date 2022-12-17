from django.shortcuts import render
# unsure if above needs to be included (was default)

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views import generic
from .models import CustomUser
from .forms import CustomUserCreationForm
from news.models import NewsStory
from django.core.exceptions import PermissionDenied
from .forms import CustomUserChangeForm

class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/createAccount.html'

class EditAccountView(generic.UpdateView):
    form_class = CustomUserChangeForm
    model = CustomUser
    context_object_name= 'createAccount'
    # fields = ['first_name', 'last_name', 'email']
    template_name = 'users/createAccount.html'
    def get_success_url(self):
        return reverse_lazy('users:AccountProfile', kwargs={'pk':self.object.id})

class AccountProfileView(generic.DetailView):
    model = CustomUser
    template_name = 'users/AccountProfile.html'
    context_object_name = 'user'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_stories'] = NewsStory.objects.filter(author=self.kwargs['pk'])
        return context


