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

    title = models.CharField(max_length=200, blank=False)
    author = models.ForeignKey(User, blank=False)
    slug = models.CharField(max_length=200, blank=False)
    content = models.TextField(default=None, blank=True)

    status = models.IntegerField(choices=STATUS_CHOICES, default=1)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(auto_now_add=True, editable=True)
    posted_at =  models.DateTimeField(blank=True, null=True, editable=True)

    def get_absolute_url(self):
        return reverse('post_update', kwargs={'post_id': self.id})