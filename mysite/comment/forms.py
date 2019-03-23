from django import forms
from home.forms import PostForm
from comment.models import Comment

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)
