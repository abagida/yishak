from django import forms

from .models import Post, Comment


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = "Title"
        self.fields['title'].widget.attrs.update({'placeholder': 'Title here'})
        self.fields['text'].label = "Content"
        self.fields['text'].widget.attrs.update({'placeholder': 'Your blog post here'})
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'})

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['author'].label = "Name"
        self.fields['author'].widget.attrs.update({'placeholder': 'Name / Surname'})
        self.fields['text'].label = "Comment"
        self.fields['text'].widget.attrs.update({'placeholder': 'Your Comment ?'})
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'})
