#_*_coding:utf-8_*_
from django import template
from ..models import Post,Category

#类实例化
register = template.Library()   

@register.simple_tag        #装饰函数，使其可以在模板中使用语法调用
#最新文章
def get_recent_posts(num=5):
    return Post.objects.all().order_by("created_time")[:num]

@register.simple_tag
#归档
def archives():
    return Post.objects.dates('created_time', 'month', order='DESC')

@register.simple_tag
#分类
def get_categories():
    return Category.objects.all()
