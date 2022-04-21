from django.contrib import admin
from .models import  Account, UserProfile, Contact, Slide, Welcome, DMCA, PrivacyPolicy, TermsOfUse, AboutUs
from django.db import models
from django.utils.html import format_html
from urllib import request
from django.contrib.auth.admin import UserAdmin


class AccountAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'username', 'last_login', 'date_joined', 'is_active')
    list_display_links = ('email', 'first_name', 'last_name')
    readonly_fields = ('last_login', 'date_joined')
    ordering = ('-date_joined',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

class UserProfileAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="30" style="border-radius:50%;">'.format(object.profile_picture.url))
    thumbnail.short_description = 'Profile Picture'
    list_display = ('thumbnail', 'user')



class SlideAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px;" />'.format(object.image.url))

    thumbnail.short_description = 'Slide Icon'    
    list_display = ["id", "thumbnail", "title", "image"]
    list_display_links = ('id', "thumbnail", "title", "image" )
    search_fields = ("id", "title" )
    formfield_overrides = {
    }

class AnnouncementAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px;" />'.format(object.image.url))

    thumbnail.short_description = 'Notice Icon'    
    list_display = ["id", "thumbnail", "subject", "image"]
    list_display_links = ('id', "thumbnail", "subject", "image" )
    search_fields = ("id", "subject" )
    formfield_overrides = {
    }

class EventAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px;" />'.format(object.image.url))

    thumbnail.short_description = 'Event Icon'    
    list_display = ["id", "thumbnail", "subject", "image"]
    list_display_links = ('id', "thumbnail", "subject", "image" )
    search_fields = ("id", "subject" )
    formfield_overrides = {
    }


admin.site.register(Account, AccountAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Contact)
admin.site.register(Slide, SlideAdmin)
admin.site.register(Welcome)
admin.site.register(DMCA)
admin.site.register(PrivacyPolicy)
admin.site.register(TermsOfUse)
admin.site.register(AboutUs)




