from django.views import generic
from .models import NewsStory


class IndexView(generic.ListView):
    template_name = 'news/index.html'

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_stories'] = NewsStory.objects.all()[:4]
        context['all_stories'] = NewsStory.objects.all()
        return context
        # This is saying get all of our news stories and use it in the index
        # latest stories = Get all news stories, but ONLY the first 4 stories (0,1,2,3) poisition
        # all_stories = all news stories

# Has a CLASS-BASED VIEW - part 4 of tutorial talk about this.
# The one's we are doing in class are class-based views
# CBW is similar to Functions but bit differemt
# 
# NOTE
# 
# Latest story
# All of the stories
# what about individual stories?
# **kwargs
# 

# MISSING:
# don't have any http response?
# Do we need to import HttpResponse?
# 