from django.contrib import admin

from django.utils.safestring import mark_safe

from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import Category, Tag, Post

class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Post
        fields = '__all__'

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    form = PostAdminForm
    save_on_top = True
    list_display = ['title', 'category', 'created_at', 'get_image']
    list_display_links = ['title', ]
    search_fields = ['title',]
    list_filter = ['category', ]
    readonly_fields = ['views', 'created_at', 'get_image']
    fields = ('title', 'slug', 'category', 'tags', 'content', 'image', 'get_image', 'views', 'created_at' )

    def get_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="64">')
        return '-'
    get_image.short_description="Слика"


admin.site.register(Category, CategoryAdmin)

admin.site.register(Tag, TagAdmin)

admin.site.register(Post, PostAdmin)

