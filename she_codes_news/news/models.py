from django.contrib.auth import get_user_model
from django.db import models


class NewsStory(models.Model):

    class Meta:
        ordering = ['-pub_date']
        


    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    pub_date = models.DateTimeField()
    image_url =  models.URLField(default="https://images6.fanpop.com/image/photos/41200000/Cat-cats-41239805-1600-900.jpg")
    # could also do in URLField(blank=True)
    content = models.TextField()


# NOTE 
# properties are title, author, pub_date
# Q: what is textfield? A: TextField doesn't have a maximum character length. Use this for long-form data.
#We have created the form not answers?
# 