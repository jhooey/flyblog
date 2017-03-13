import datetime

from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseForbidden, HttpResponse

from blog.models import Post
from blog.forms import PostForm


#all users to logout. We currently only support super users
from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    
    return redirect('blog')
    
#main page. Lists all of the posted blog posts
def blog(request):
    posts = Post.objects.all().filter(status=2).order_by('-created_at')
    return render(request, 'blog/blog.html', {'posts':posts})


#Lists all of the unpublished blog posts
@login_required
def drafts(request):
    posts = Post.objects.all().filter(status=1).order_by('-created_at')
    return render(request, 'blog/drafts.html', {'posts':posts})
  

#Creates a post for you so that you can start editing
@login_required
def create_post(request):
    post = Post.objects.create(author = request.user,)
    post.save()
    
    return redirect(post)

#Any changes to a post must pass through this view
@login_required
def update_post(request, post_id):
    post=Post.objects.get(id=post_id)
    post_form = PostForm(instance=post)
    
    if post.author != request.user:
        return HttpResponseForbidden()
    
    if request.method=='POST':
        post_form = PostForm(request.POST, instance=post)
        if post_form.is_valid():
            post= post_form.save(commit=False)
            post.modified_at = datetime.datetime.now()
            post.save()  
            success = True   
            
            if request.is_ajax():
                return HttpResponse("Success")
            else:     
                messages.success(request, 'Post Updated Successfully') 
        elif request.is_ajax():
            return HttpResponse("Fail")
            
    return render(request, 'blog/update_post.html', {'post':post, 'form': post_form})


#Updates the post status to Posted
@login_required
def publish_post(request, post_id):
    post=Post.objects.get(id=post_id)
    
    if post.author != request.user:
        return HttpResponseForbidden()
    
    try:
        post.status = 2
        post.posted_at = datetime.datetime.now()
        post.save()
        messages.success(request, 'Post Published Successfully') 
        return redirect('blog')
        
    except Exception:
        messages.error(request, 'Post not Published')
        
    return redirect(post)
    
    
    
#Changes the post status to Archived. Nothing is truly deleted
@login_required
def delete_post(request, post_id):
    post=Post.objects.get(id=post_id)
    
    if post.author != request.user:
        return HttpResponseForbidden()


    try:
        post.status = 3
        post.modified_at = datetime.datetime.now()
        post.save()
        messages.success(request, 'Post Deleted Successfully') 
        return redirect('blog')
        
    except Exception:
        messages.error(request, 'Post not Deleted')
        
    return redirect(post)