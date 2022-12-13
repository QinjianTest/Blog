# @Auth:qinjian
# @Time:2022/03/01 19:51

"""
主体表结构
UserInfo
Avatars
...
"""
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import pre_delete  # 删除文件
from django.dispatch.dispatcher import receiver  # 删除文件
from django.utils.html import format_html

# 文章表
class Articles(models.Model):
    """
    title：文章标题
    abstract：文章简介
    content：文章内容
    create_date：创建日期
    change_date：编辑的最新日期
    status：文章的状态，默认都是已发布
    recommend：是否上推荐
    cover：文章封面  一对多
    look_count：浏览量
    comment_count：评论数
    digg_count：点赞数
    collects_count：收藏数
    category：文章分类
    tag：文章标签 多对多
    pwd：文章密码
    author：文章的作者  后续可以做一对多，关联用户表
    source：文章的来源
    link：来源地址
    word：文章字数
    """
    nid = models.AutoField(primary_key=True)
    title = models.CharField(verbose_name='标题', max_length=32, null=True, blank=True)
    abstract = models.CharField(verbose_name='文章简介', max_length=128, null=True, blank=True)
    content = models.TextField(verbose_name='文章内容', null=True, blank=True)
    create_date = models.DateTimeField(verbose_name='文章发布日期', auto_now_add=True, null=True)
    change_date = models.DateTimeField(verbose_name='文章修改日期', auto_now=True, null=True)
    status_choice = (
        (0, '未发布'),
        (1, '已发布'),
    )
    status = models.IntegerField(verbose_name='文章保存状态', choices=status_choice)
    cover_id = models.CharField(verbose_name='文章封面ID', max_length=16,null=True, default="01")
    # cover = models.ForeignKey(
    #     to='Cover',
    #     to_field='nid',
    #     on_delete=models.SET_NULL,
    #     verbose_name='文章封面', null=True, blank=True
    # )
    recommend = models.BooleanField(verbose_name='是否上推荐', default=None)
    look_count = models.IntegerField(verbose_name='文章阅读量', default=0)
    comment_count = models.IntegerField(verbose_name='文章评论量', default=0)
    digg_count = models.IntegerField(verbose_name='文章点赞量', default=0)
    collects_count = models.IntegerField(verbose_name='文章收藏数', default=0)
    category_choice = (
        (1, '技术'),
        (2, '生活'),
    )
    category = models.IntegerField(verbose_name='文章分类', choices=category_choice, null=True, blank=True)
    tag = models.CharField(max_length=32, verbose_name='标签', null=True, blank=True)
    pwd = models.CharField(max_length=32, verbose_name='文章密码', null=True, blank=True)
    author = models.CharField(max_length=16, verbose_name='作者', null=True, blank=True)
    source = models.CharField(max_length=32, verbose_name='来源', null=True, blank=True)

    link = models.URLField(verbose_name='文章链接', null=True, blank=True)
    word = models.IntegerField(verbose_name='文章字数', default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = '文章'

# class Cover(models.Model):
#     nid = models.AutoField(primary_key=True)
#     url = models.FileField(verbose_name='文章封面地址', upload_to='article_img/')
#     dominant_hue = models.CharField(verbose_name='封面主色调', max_length=16, null=True, blank=True)
#     is_dark = models.BooleanField(verbose_name='是否是深色系', null=True, blank=True)
#
#     def __str__(self):
#         return str(self.url)
#
#     class Meta:
#         verbose_name_plural = '文章封面'

# 生活记录
# class Moods(models.Model):
#     nid = models.AutoField(primary_key=True)
#     name = models.CharField(verbose_name='发布人', max_length=16)
#     ip = models.GenericIPAddressField(verbose_name='ip地址', default='127.0.0.1')
#     addr = models.TextField(verbose_name='用户地址信息', null=True)
#     create_date = models.DateTimeField(verbose_name='发布时间', auto_now=True)
#     content = models.TextField(verbose_name='心情内容')
#     drawing = models.TextField(verbose_name='配图组，以;隔开', null=True, blank=True)
#     comment_count = models.IntegerField(verbose_name='评论数', default=0)
#     digg_count = models.IntegerField(verbose_name='点赞数', default=0)
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name_plural = '心情'


