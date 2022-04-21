from django.contrib import admin
from school.models import Category, Post, Comment, Reply
from django.db import models
from django.utils.html import format_html
from embed_video.admin import AdminVideoMixin


class CategoryAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px;" />'.format(object.image.url))

    thumbnail.short_description = 'Category Icon'    
    list_display = ["id", "thumbnail", "category_name", "slug", "image" ]
    list_display_links = ('id', "thumbnail", "category_name" )
    prepopulated_fields = {'slug': ('category_name',)}
    search_fields = ('id', "category_name" )
    list_filter = ('category_name', )
    formfield_overrides = {
   
    }



class PostAdmin(AdminVideoMixin, admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px;" />'.format(object.image.url))

    thumbnail.short_description = 'Post Icon'    
    list_display = ["post_id", "thumbnail", "name", "created_by", "created_at", "category" ]
    list_display_links = ("post_id", "thumbnail", "name", "category" )
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('post_id', "name", "created_by", "created_at", "category" )
    list_filter = ("name", "created_by", "created_at", "category" )
    formfield_overrides = {
    
    }


class CommentAdmin(admin.ModelAdmin):
    list_display = ["body", "user", "post_name", "date_added"]
    search_fields = ('body', "user", "date_added", "post_name")
    list_filter = ('body', "user", "date_added", "post_name")
    formfield_overrides = {
    }

    
class ReplyAdmin(admin.ModelAdmin):
    list_display = ["reply_body", "user", "date_added"]
    search_fields = ('reply_body', "user", "date_added")
    list_filter = ('reply_body', "user", "date_added")
    formfield_overrides = {
    }



admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Reply, ReplyAdmin)


