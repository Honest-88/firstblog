from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
import email
import os
from django.contrib.auth.models import User

class MyAccountManager(BaseUserManager):
    def create_user(self, first_name, last_name, username, email, password=None):
        if not email:
            raise ValueError('User must have an email address')

        if not username:
            raise ValueError('User must have a username')

        user = self.model(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, email, username, password):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password = password,
            first_name = first_name,
            last_name = last_name,
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    first_name      = models.CharField(max_length=50)
    last_name       = models.CharField(max_length=50)
    username        = models.CharField(max_length=50, unique=True)
    email           = models.EmailField(max_length=100, unique=True)
    # required
    date_joined     = models.DateTimeField(auto_now_add=True)
    last_login      = models.DateTimeField(auto_now_add=True)
    is_admin        = models.BooleanField(default=False)
    is_staff        = models.BooleanField(default=False)
    is_active       = models.BooleanField(default=False)
    is_superadmin   = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    objects = MyAccountManager()

    class Meta:
        verbose_name = 'User Accounts'
        verbose_name_plural = 'User Accounts'

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True


class UserProfile(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE)
    profile_picture = models.ImageField(blank=True, upload_to='userprofile')
    
    class Meta:
        verbose_name = 'User Profiles'
        verbose_name_plural = 'User Profiles'


    def __str__(self):
        return self.user.first_name


class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200, blank=True, null=True)
    feedback = models.TextField()

    class Meta:
        verbose_name = 'Contact Us'
        verbose_name_plural = 'Contact Us' 


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('index')
        
class Slide(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    motto = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='Images/', blank=True, null=True)

    def __str__(self):
        return self.title


class Welcome(models.Model):
    id = models.AutoField(primary_key=True)
    title1 = models.CharField(max_length=200, blank=True, null=True)
    title2 = models.CharField(max_length=200, blank=True, null=True)
    motto = models.CharField(max_length=500, blank=True, null=True)
   

    def __str__(self):
        return self.motto


class DMCA(models.Model):
    id = models.AutoField(primary_key=True)
    subject = models.CharField(max_length=200, blank=True, null=True)
    about = HTMLField(blank=True, null=True)
    image = models.ImageField(upload_to='Images/', blank=True, null=True)

    class Meta:
        verbose_name = 'Digital Millennium Copyright Act'
        verbose_name_plural = 'Digital Millennium Copyright Act'

    def __str__(self):
        return self.subject


class PrivacyPolicy(models.Model):
    id = models.AutoField(primary_key=True)
    subject = models.CharField(max_length=200, blank=True, null=True)
    about = HTMLField(blank=True, null=True)
    image = models.ImageField(upload_to='Images/', blank=True, null=True)

    class Meta:
        verbose_name = 'Our Privacy Policy'
        verbose_name_plural = 'Our Privacy Policy'

    def __str__(self):
        return self.subject


class TermsOfUse(models.Model):
    id = models.AutoField(primary_key=True)
    subject = models.CharField(max_length=200, blank=True, null=True)
    about = HTMLField(blank=True, null=True)
    image = models.ImageField(upload_to='Images/', blank=True, null=True)

    class Meta:
        verbose_name = 'Terms Of Use'
        verbose_name_plural = 'Terms Of Use'

    def __str__(self):
        return self.subject

class AboutUs(models.Model):
    id = models.AutoField(primary_key=True)
    subject = models.CharField(max_length=200, blank=True, null=True)
    about = HTMLField(blank=True, null=True)
    image = models.ImageField(upload_to='Images/', blank=True, null=True)

    class Meta:
        verbose_name = 'About Us'
        verbose_name_plural = 'About Us'


    def __str__(self):
        return self.subject



