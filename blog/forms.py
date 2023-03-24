from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        # the comma is important, otherwise python will read it as
        # string instead of a tuple.
        fields = ('body',)
