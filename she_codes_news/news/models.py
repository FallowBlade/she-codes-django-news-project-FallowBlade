from django.contrib.auth import get_user_model
from django.db import models


class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    # author = models.CharField(max_length=200)
    author = models.ForeignKey(get_user_model(),
    on_delete=models.CASCADE)
    pub_date = models.DateTimeField()
    content = models.TextField()

# NOTE 
# properties are title, author, pub_date
# Q: what is textfield? A: TextField doesn't have a maximum character length. Use this for long-form data.
#We have created the form not answers?
# 