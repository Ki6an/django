from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# creating db models 
class Post(models.Model):
    # title can be set only to 100 chars
    title = models.CharField(max_length=100)
    content = models.TextField()  # unlimited text filed ofc
    # records the time when the post was created
    date_posted = models.DateTimeField(default=timezone.now)
    # gives one to many relationship if the user
    # is deleted then the post relating to them is deleted.
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

  
