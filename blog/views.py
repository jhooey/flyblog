from django.shortcuts import redirect, render
from blog.models import Post
# Create your views here.
def blog(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blog/blog.html', {'posts':posts})

def create_post(request):
    post = Post.objects.create(title = "title", author = request.user, content = "content", slug = "slug")
    post.save()
    
    return redirect('update_post', {})

def update_post(request, post_id):
    post=Post.objects.get(id=post_id)
    return render(request, 'blog/update_post.html', {'post':post})