from django.contrib import admin
from django import forms
from ckeditor.widgets import CKEditorWidget

from posts.models import Post
from main.admin import ibeeam_site


class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Post
        fields = ('user', 'title', 'content')


class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm

ibeeam_site.register(Post, PostAdmin)
