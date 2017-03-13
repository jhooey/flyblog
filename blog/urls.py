from django.conf.urls import url

from blog import views


urlpatterns = [
    url(r'^blog', views.blog, name='blog'),
    url(r'^create_post', views.create_post, name='create_post'),
    url(r'^(?P<post_id>[\w-]+)/update_post', views.update_post, name='update_post'),
    ]
