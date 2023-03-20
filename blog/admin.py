from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    # we will fill in the slug field with prepopulated text from title field
    prepopulated_fields = {'slug': ('title',)}
    # we will add a filter to filter posts
    list_filter = ('status', 'created_on')
    # we display the title, slug, status and created_on
    list_display = ('title', 'slug', 'status', 'created_on')
    # we add searchfields to search after title and content
    search_fields = ['title', 'content']
    summernote_fields = ('content')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)


# the following method get's removed, since it allows us only to add
# two arguments, which is not enough. Therefore we have create the
# decorator just above the PostAdmin class.

# admin.site.register(Post)
