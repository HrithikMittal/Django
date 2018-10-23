from django.conf.urls import url
from . import views
from django.urls import include, path
app_name = 'groups'

urlpatterns = [
    url(r'^$',views.ListGroups.as_view(),name='all'),
    url(r'new/$',views.CreateGroup.as_view(),name='create'),
    url(r'posts/in/(?P<slug>[-\w]+)/$',views.SingleGroup.as_view(),name='single'),
    url(r'leave/(?P<slug>[-\w]+)/$',views.LeaveGroup.as_view(),name='leave'),
    url(r'join/(?P<slug>[-\w]+)/$',views.JoinGroup.as_view(),name='join'),

    #url(r'posts/create/', include('posts.urls')),
]
