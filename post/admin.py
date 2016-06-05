from django.contrib import admin
from post.models import Post, Comment, Category

class CommentsInLine(admin.StackedInline):
    model = Comment
    extra = 3

class PostAdmin(admin.ModelAdmin):
    inlines = [CommentsInLine]
# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Category)
