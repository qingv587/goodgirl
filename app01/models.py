from django.db import models

# Create your models here.
class UserInfo(models.Model):
    username = models.CharField(max_length=32,verbose_name="用户名")
    nickname = models.CharField(max_length=32,verbose_name="昵称")
    password = models.CharField(max_length=64,verbose_name="密码")
    email = models.EmailField(verbose_name="邮箱")
    img = models.FileField(verbose_name="头像",null=True,blank=True)
    concerner = models.ManyToManyField("userinfo",verbose_name="关注",through="user2user",through_fields=("user1","user2"))

class Blog(models.Model):
    user = models.OneToOneField("userinfo")
    title = models.CharField(max_length=64,verbose_name="个性签名")
    site = models.CharField(max_length=32,verbose_name="后缀")

class Catagory(models.Model):
    title = models.CharField(max_length=32,verbose_name="分类")
    site = models.CharField(max_length=32,verbose_name="分类后缀")

class PersonCatagory(models.Model):
    title = models.CharField(max_length=32, verbose_name="个人分类")
    blog = models.ForeignKey("blog")

class Tag(models.Model):
    title = models.CharField(max_length=32, verbose_name="标签")
    blog = models.ForeignKey("blog")

class Article(models.Model):
    title = models.CharField(max_length=128,verbose_name="标题")
    summary = models.TextField(verbose_name="简介")
    blog = models.ForeignKey("blog")
    catagory = models.ForeignKey("catagory")
    personcatagory = models.ForeignKey("personcatagory")
    tag = models.ManyToManyField("tag")
    up = models.IntegerField(verbose_name="赞",default=0,null=True,blank=True)
    down = models.IntegerField(verbose_name="踩",default=0,null=True,blank=True)
    create_time = models.DateTimeField(verbose_name="创建时间")

class Comment(models.Model):
    article = models.ForeignKey("article")
    content = models.TextField(verbose_name="评论")
    create_time = models.DateTimeField(verbose_name="创建时间")
    parent = models.ManyToManyField("comment",null=True,blank=True)

class Content(models.Model):
    article = models.OneToOneField("article")
    text = models.TextField(verbose_name="文章内容")

class Tag2Aticle(models.Model):
    aticle = models.ForeignKey("article")
    tag = models.ForeignKey("tag")
    class Meta:
        unique_together = ("aticle","tag")

class User2User(models.Model):
    user1 = models.ForeignKey("userinfo",related_name="user")
    user2 = models.ForeignKey("userinfo",related_name="fan")
    class Meta:
        unique_together = ("user1","user2")