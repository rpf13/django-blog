# First we need to import our views from the current directory
from . import views
from django.urls import path


# Creating the view with a blank path (empty string), means its our default
# Since we use class based views, we need to add the .as_view method
# at the end of it.
urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>/', views.PostLike.as_view(), name='post_like'),
]
