from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


# Create your models here.

class Category(models.Model):
    """文章分类"""
    name = models.CharField(max_length=100, verbose_name="博客分类")
    index = models.IntegerField(default=999, verbose_name="分类排序")

    class Meta:
        verbose_name = "博客分类"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Tag(models.Model):
    """文章标签"""
    name = models.CharField(max_length=100, verbose_name="文章标签")

    class Meta:
        verbose_name = "文章标签"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Tui(models.Model):
    """推荐位"""
    name = models.CharField(max_length=100, verbose_name="推荐位")

    class Meta:
        verbose_name = "推荐位"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Article(models.Model):
    """文章"""
    title = models.CharField(max_length=70, verbose_name="标题")
    excerpt = models.TextField(max_length=200, blank=True, verbose_name="摘要")
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, verbose_name='分类', blank=True, null=True)
    # 使用外键关联分类表与分类是一对多关系
    tags = models.ManyToManyField(Tag, verbose_name='标签', blank=True)
    # 使用外键关联标签表与标签是多对多关系
    img = models.ImageField(upload_to='article_img/%Y/%m/%d/', verbose_name='文章图片', blank=True, null=True)
    # body = models.TextField()
    content = RichTextField(verbose_name='内容')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='作者')
    """
    文章作者，这里User是从django.contrib.auth.models导入的。
    这里我们通过 ForeignKey 把文章和 User 关联了起来。
    """
    views = models.PositiveIntegerField(verbose_name='阅读量', default=0)
    tui = models.ForeignKey(Tui, on_delete=models.DO_NOTHING, verbose_name='推荐位', blank=True, null=True)

    created_time = models.DateTimeField(verbose_name='发布时间', auto_now_add=True)
    modified_time = models.DateTimeField(verbose_name='修改时间', auto_now=True)

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Banner(models.Model):
    """轮播图"""
    text_info = models.CharField(verbose_name='标题', max_length=50, default='')
    img = models.ImageField(verbose_name='轮播图', upload_to='banner/')
    link_url = models.URLField(verbose_name='图片链接', max_length=100)
    is_active = models.BooleanField(verbose_name='是否是active', default=False)

    def __str__(self):
        return self.text_info

    class Meta:
        verbose_name = '轮播图'
        verbose_name_plural = verbose_name


#
class Link(models.Model):
    """友情链接"""
    name = models.CharField(verbose_name='链接名称', max_length=20)
    linkurl = models.URLField(verbose_name='网址', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '友情链接'
        verbose_name_plural = verbose_name
