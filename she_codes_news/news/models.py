from django.contrib.auth import get_user_model
from django.db import models


class NewsStory(models.Model):

    class Meta:
        ordering = ['-pub_date', 'author']

    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    pub_date = models.DateTimeField()
    image_url =  models.URLField(blank=True)
    # could also do in URLField(blank=True)
    content = models.TextField()
    


# NOTE 
# this is the only file that talks to the database - so you need to make migrations and then migrate to ensure it is connected.
# properties are title, author, pub_date
# Q: what is textfield? A: TextField doesn't have a maximum character length. Use this for long-form data.
#We have created the form not answers?
