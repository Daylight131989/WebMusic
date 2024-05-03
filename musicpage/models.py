from django.db import models
from datetime import date, datetime
 
 
# Create your models here.
class Singler(models.Model):
    """ 歌手表模型 """
 
    name = models.CharField(max_length=50, help_text='请输入歌手名称')
    first_letter = models.CharField(max_length=15, help_text='请输入歌手名称首字母')
    # 设置上传位置
    portrait = models.ImageField(upload_to='uploads/singer_portrait/%Y%m%d/', help_text='请上传歌手照片')
    birthday = models.DateField(default=date.today, help_text='请选择歌手生日')
    height = models.IntegerField(help_text='请输入歌手身高（cm）', default=0, blank=True)
    weight = models.IntegerField(help_text='请输入歌手体重（kg）', default=0, blank=True)
    constellation = models.CharField(max_length=50, help_text='请输入歌手星座')
    singe_num = models.IntegerField(default=0)
    album_num = models.IntegerField(default=0)
    desc = models.TextField(help_text='请输入歌手简介')
    addtime = models.DateTimeField(auto_now_add=True)
    updatetime = models.DateTimeField(auto_now=True)

class Singe(models.Model):
    """ 单曲表 """
 
    name = models.CharField(max_length=50, help_text='请输入单曲名称')
    duration = models.IntegerField(help_text='请输入歌曲时长（ms）')
    path = models.FileField(upload_to='uploads/songs_path/%Y%m%d/', help_text='请上传歌曲')
    lyric = models.FileField(upload_to='uploads/songs_lyric/%Y%m%d/', help_text='请上传歌曲单词')
    addtime = models.DateTimeField(auto_now_add=True)
    updatetime = models.DateTimeField(auto_now=True)
 
    # 设置与歌手表关联外键
    # 一对多外键设置在多的模型中
    singler = models.ForeignKey("Singler", on_delete=models.CASCADE)
 
 
class Album(models.Model):
    """ 专辑表 """
 
    name = models.CharField(max_length=50, help_text='请输入专辑名称')
    cover = models.ImageField(upload_to='uploads/album_cover/%Y%m%d/', help_text='请上传专辑封面图')
    desc = models.CharField(max_length=255, help_text='请输入专辑描述')
    single_num = models.IntegerField(default=0, help_text='请输入单曲数')
    single_lang = models.CharField(max_length=50, help_text='请输入专辑语种')
    addtime = models.DateTimeField(auto_now_add=True)
    updatetime = models.DateTimeField(auto_now=True)
 
    # 设置与歌手表关联外键 一对多 级联删除
    singler = models.ForeignKey("Singler", on_delete=models.CASCADE)
 
    # 设置与单曲表关联外键 多对多
    Singe = models.ManyToManyField('Singe')


class Carousel(models.Model):
    """ 首页轮播图 """
 
    path = models.ImageField(upload_to='uploads/carousel_cover/%Y%m%d/', help_text='请选择上传首页轮播图')
    href = models.CharField(max_length=100, help_text='请输入点击图片后跳转路径')


class SongCategory(models.Model):
    """ 歌曲类型表 """
 
    name = models.CharField(max_length=100, help_text='请输入类型名称')
    pid = models.IntegerField(default=0, help_text='父类型id')
 
 
class SongSheet(models.Model):
    """ 歌单表 """
 
    name = models.CharField(max_length=100, help_text='请输入歌单名称')
    cover = models.ImageField(upload_to='uploads/sheet_cover/%Y%m%d/', help_text='请上传歌单封面图')
    playnum = models.IntegerField(default=0, help_text='请输入播放量')
    
    addtime = models.DateTimeField(auto_now_add=True)
    updatetime = models.DateTimeField(auto_now=True)
 
    # 歌曲类型与歌单表 多对多关系
    category = models.ManyToManyField('SongCategory')
 
    # 歌单表与单曲表多对多关系
    singe = models.ManyToManyField('Singe')