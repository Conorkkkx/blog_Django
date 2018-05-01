# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.six import python_2_unicode_compatible

@python_2_unicode_compatible
class Category(models.Model): 
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

@python_2_unicode_compatible   
class Tag(models.Model): 
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Post(models.Model):
    # 文章标题
    title = models.CharField(max_length=100)
    # 文章正文
    body = models.TextField()
    # 创建时间
    created_time = models.DateTimeField()
    # 修改时间
    modified_time = models.DateTimeField()
    # 文章摘要
    # blank=True 参数值后就可以允许空值了。
    excerpt = models.CharField(max_length=200, blank=True)
    # 文章标签
    category = models.ForeignKey(Category)
    # 文章分类
    tags = models.ManyToManyField(Tag, blank=True)
    # 文章作者
    author = models.ForeignKey(User)
    #文章阅读量
    views = models.PositiveIntegerField(default=0)
    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})
    class Meta:
      #  ordering = ['created_time']
        ordering = ['-created_time','title']
