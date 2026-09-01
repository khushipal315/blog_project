from django import forms
from .models import BlogPost


class BlogPostForm(forms.ModelForm):

    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'image']

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter blog title'
            }),

            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Write your blog here...',
                'rows': 8
            }),

            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
        }