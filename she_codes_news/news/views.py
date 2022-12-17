from django.views import generic
from django.urls import reverse_lazy
from .models import NewsStory
from .forms import StoryForm
from users.models import CustomUser
from django.core.exceptions import PermissionDenied

class IndexView(generic.ListView):
    template_name = 'news/index.html'

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_stories'] = NewsStory.objects.all()[:6]
        # context['all_stories'] = NewsStory.objects.all()
        context['old_stories'] = NewsStory.objects.all().order_by('pub_date')[:6]
        context['news_author'] = CustomUser.objects.all()
        # old_stories orders your news stories by date.
        return context
        # This is saying get all of our news stories and use it in the index
        # latest stories = Get all news stories, but ONLY the first 4 stories (0,1,2,3) poisition
        # all_stories = all news stories


# how to move what you want on your news page.


class AddStoryView(generic.CreateView):
    form_class = StoryForm
    context_object_name = 'storyForm'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')

    def form_valid(self, form):
            form.instance.author = self.request.user
            return super().form_valid(form)

class StoryView(generic.DetailView):
	model = NewsStory
	template_name = 'news/story.html'
	context_object_name = 'story'


class DeleteStoryView(generic.DeleteView):
    model = NewsStory
    template_name= "news/deleteStory.html"
    success_url = reverse_lazy('news:index')

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.author != self.request.user:
            raise PermissionDenied 
        return obj

#EDIT STORY
#If I'm not the owner of story, I can't edit
class EditStoryView(generic.UpdateView):
    model=NewsStory
    form_class = StoryForm
    # fields = ['title', 'pub_date', 'category', 'content']
    template_name= "news/createStory.html"
    context_object_name="storyForm"
    success_url= reverse_lazy('news:index')

    def get_object(self, queryset=None):
        obj=super().get_object(queryset)
        if obj.author != self.request.user:
                raise PermissionDenied
        return obj
    # def img_form(request)
    #     form.instance.image_url = self.request.form
    #     return render( request, ).img_form(form)

# Has a CLASS-BASED VIEW - part 4 of tutorial talk about this.
# The one's we are doing in class are class-based views
# CBW is similar to Functions but bit differemt
# 
# NOTE
#6/12/22 BUG - was able to determine that Django error exception when trying to run form was due to the fact that the template_name was not properly defined. I had input template_name: 'news/CreateStory.html' instead of template_name = 


# Latest story
# All of the stories
# what about individual stories?
# **kwargs
# 

# MISSING:
# don't have any http response?
# Do we need to import HttpResponse?
# 