from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.contrib.auth.models import User
import os
from embed_video.fields import EmbedVideoField
from tinymce.models import HTMLField
from taggit.managers import TaggableManager
from users.models import Account

def save_category_image(instance, filename):
    upload_to = 'Images/'
    ext = filename.split('.')[-1]
    #Get filename
    if instance.category_id:
        filename = 'Category_Picture/{}.{}'.format(instance.category_id, ext)
    return os.path.join(upload_to, filename)



class Category(models.Model):   #category #subject
    id = models.AutoField(primary_key=True)
    category_id = models.CharField(max_length=200, unique=True)
    category_name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True , null=True, blank=True)
    image = models.ImageField(upload_to=save_category_image, blank=True, verbose_name='Category Image')
    description = HTMLField(max_length=1000, blank=True, null=True)


    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category_name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.category_id)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('school:post_list', args=[self.id,])

def save_post_files(instance, filename):
    upload_to = 'Images/'
    ext = filename.split('.')[-1]
    #Get filename
    if instance.post_id:
        fielname = 'post_files/{}/{}.{}'.format(instance.post_id, instance.post_id, ext)
        if os.path.exists(filename):
            new_name = str(instance.post_id) + str('1')
            filename = 'Post_images/{}/{}.{}'.format(instance.post_id, new_name, ext)
    return os.path.join(upload_to, filename)


class Post(models.Model): #POst list #lesson
    id = models.AutoField(primary_key=True)
    tags = TaggableManager()
    post_id = models.CharField(max_length=200, unique=True)
    created_by = models.ForeignKey(Account, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')
    name = models.CharField(max_length=250)
    position = models.PositiveBigIntegerField(verbose_name="Post no.")
    slug = models.SlugField(unique=True, null=True, blank=True)
    image = models.ImageField(upload_to=save_post_files, blank=True, verbose_name='Post Image')
    description = HTMLField(blank=True, null=True)
    videolink = EmbedVideoField(verbose_name="Video link", blank=True, null=True)  
    filelink = models.URLField(blank=True, null=True)
    


    class Meta:
        ordering = ['-position']

    def __str__(self):
        return self.name

    def total_views(self):
        return self.views.count()


    def total_likes(self):
        return self.likes.count()


    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('school:post_list', args=[self.id,])


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    post_name = models.ForeignKey(Post, null=True, on_delete=models.CASCADE, related_name='comments')
    comm_name = models.CharField(max_length=200, blank=True)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    body = models.TextField(max_length=1000)
    date_added = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.comm_name = slugify("comment by" + "-" + str(self.user) + str(self.date_added))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.comm_name

    class Meta:
        ordering = ['-date_added']

    
class Reply(models.Model):
    id = models.AutoField(primary_key=True)
    comment_name = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='replies')
    reply_body = models.TextField(max_length=500)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name = 'Reply'
        verbose_name_plural = 'Replies'

    def __str__(self):
        return "reply to " + str(self.comment_name.comm_name)







