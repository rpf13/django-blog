from django.shortcuts import render, get_object_or_404
from django.views import generic, View
# We have to import the model and the related class
# for which we want to create a view.
from .models import Post


# This view is based on the Django generic predefined views.
# It will inherit from the generic.ListView
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


# We add another view, this time not one of the Django predefine generic ones
# It will inherit from the View module.
class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        # in order to get a particular post, we need to identify it
        # which we can do based on the slug, which is unique
        # then we filter based on the published ones
        queryset = Post.objects.filter(status=1)
        # Then we get the acutal object based on the slug
        post = get_object_or_404(queryset, slug=slug)
        # The post object contains most of useful content we need
        # like the comments
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        # We then return / send our request to get rendered by our template
        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "liked": liked
            },
        )
