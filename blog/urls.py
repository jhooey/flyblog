from django.conf.urls import url

from blog import views


urlpatterns = [
    url(r'^$', views.blog, name='blog'),
    url(r'^logout', views.logout_view, name='logout'),
    url(r'^create_post', views.create_post, name='create_post'),
    url(r'^(?P<post_id>[\w-]+)/update_post', views.update_post, name='update_post'),
    url(r'^(?P<post_id>[\w-]+)/publish_post', views.publish_post, name='publish_post'),
    url(r'^(?P<post_id>[\w-]+)/delete_post', views.delete_post, name='delete_post'),
    url(r'^drafts', views.drafts, name='drafts'),
    ]
