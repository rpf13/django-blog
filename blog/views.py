from django.shortcuts import render
from django.views import generic
# We have to import the model and the related class
# for which we want to create a view.
from .models import Post


class PostList(generic.ListView):
    model = Post
    # we only display the published post (status = 1, 0 = draft) and
    # we sort in descending order
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    # Template name, which our view will render
    template_name = 'index.html'
    # The generic ListView includes a default set of posts visible on
    # one page, called "pagination". We set it here to 6 posts. If there
    # is more, Django will create autom. a page navigation.
    paginate_by = 6
