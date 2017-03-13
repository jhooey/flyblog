from django.db import models
from django.contrib.auth.models import User

from django.core.urlresolvers import reverse


# Create your models here.
class Post(models.Model):

    STATUS_CHOICES = (
        (1, 'Draft'),
        (2, 'Posted'),
        (3, 'Archive'),
    )

    author = models.ForeignKey(User, blank=False) #automatically set to the logged in user
    
    #Post Content
    title = models.CharField(max_length=200, blank=False, default='Title')
    content = models.TextField(default="", blank=True)

    #Status is used to handle where a post is being displayed
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)

    #record keeping - if we wanted to track all modifications a separate table 
    #                 for modification dates is needed
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(auto_now_add=True, editable=True)
    posted_at =  models.DateTimeField(blank=True, null=True, editable=True)

    def get_absolute_url(self):
        return reverse('update_post', kwargs={'post_id': self.id})
    
    #Needed to easily identify the posts in the admin console
    def __str__(self):
        return self.title
    