from django.forms.models import ModelForm

from blog.models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        exclude = ['author', 'status', 'created_at', 'modified_at', 'posted_at']