from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# creating db models


class Post(models.Model):
    # title can be set only to 100 chars
    title = models.CharField(max_length=100)
    content = models.TextField()  # unlimited text filed ofc
    # records the time when the post was created and can be updated
    date_posted = models.DateTimeField(default=timezone.now)
    # gives one to many relationship if the user
    # is deleted then the post relating to them is deleted.
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):   # gives the location to the post that was created 
        return reverse('post-detail', kwargs={'pk': self.pk})
