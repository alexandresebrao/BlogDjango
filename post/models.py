from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    def __unicode__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    category = models.ForeignKey(Category)
    date = models.DateTimeField(auto_now=True)
    def __unicode__(self):
        return self.title
    def comments(self):
        return Comments.objects.get(post=self).order_by('-date')

class Comment(models.Model):
    body = models.TextField()
    user = models.ForeignKey(User)
    date = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(Post)
    def __unicode__(self):
        return "%s - %s" %(self.user.username, self.post)
