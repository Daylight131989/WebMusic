from django.db import models
from datetime import date, datetime
from xpinyin import Pinyin
import time
import eyed3
import os
from django.conf import settings

def get_singe_singler_num(singler_id):
    """
    获取单曲表中所属歌手数
    :param singler_id:
    :return:
    """
    return Singe.objects.filter(singler_id=singler_id).count()

def get_duration_mp3(file_path):
        """ 获取mp3音频文件时长 """
    
        info = eyed3.load(file_path)
        return info.info.time_secs

def get_first_letter(name):
    """获取姓名中的首字母"""

    obj = Pinyin()
    name_pinyin = obj.get_pinyin(name, '')
    return name_pinyin[0]

def get_album_singler_num(singler_id):
    """
    获取专辑表中所属歌手数
    :param singler_id:
    :return:
    """
    return Album.objects.filter(singler_id=singler_id).count()

class BaseModel(models.Model):
    """ 设置基础模型类 """

    addtime = models.DateTimeField(auto_now_add=True)
    updatetime = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
 
# Create your models here.
class Singler(BaseModel):
    """ 歌手表模型 """
    
    def __str__(self):
        """ 修改返回格式 """
        return self.name

    def upload_save_path_singer_portrait(instance, filename):
        """ 上传文件保存路径 """
        # 获取当前日期并格式化为YYYYMMDD形式的字符串
        date_string = time.strftime("%Y%m%d", time.localtime())
        return 'uploads/singer_portrait/' + date_string + '/{0}'.format(filename)
 
    class Meta:
        verbose_name = '歌手'
        verbose_name_plural = '歌手'

    name = models.CharField(max_length=50, help_text='请输入歌手名称', verbose_name = '姓名')
    first_letter = models.CharField(max_length=15, help_text='请输入歌手名称首字母', verbose_name = '姓名首字母')
    # 设置上传位置
    portrait = models.ImageField(upload_to=upload_save_path_singer_portrait, help_text='请上传歌手照片', verbose_name = '照片')
    birthday = models.DateField(default=date.today, help_text='请选择歌手生日', verbose_name = '生日')
    height = models.IntegerField(help_text='请输入歌手身高（cm）', default=0, blank=True, verbose_name = '身高(cm)')
    weight = models.IntegerField(help_text='请输入歌手体重（kg）', default=0, blank=True, verbose_name = '体重(kg)')
    constellation = models.CharField(max_length=50, help_text='请输入歌手星座', verbose_name = '星座')
    singe_num = models.IntegerField(default=0, editable = False)
    album_num = models.IntegerField(default=0, editable = False)
    desc = models.TextField(help_text='请输入歌手简介', verbose_name = '简介')

    def save(self, froce_insert=False, force_update=False, using=None, update_fields=None):
        """重写save方法"""

        self.first_letter = get_first_letter(self.name)
        super().save()

class Singe(BaseModel):
    """ 单曲表 """
    
    def upload_save_path_songs_path(instance, filename):
        """ 上传文件保存路径 """
        date_string = time.strftime("%Y%m%d", time.localtime())
        return 'uploads/songs_path/' + date_string + '/{0}'.format(filename)

    def upload_save_path_songs_lyric(instance, filename):
        """ 上传文件保存路径 """
        date_string = time.strftime("%Y%m%d", time.localtime())
        return 'uploads/songs_lyric/' + date_string + '/{0}'.format(filename)

    class Meta:
        verbose_name = '单曲'
        verbose_name_plural = '单曲'

    name = models.CharField(max_length=50, help_text='请输入单曲名称', verbose_name = '单曲名称')
    duration = models.IntegerField(editable=False)
    path = models.FileField(upload_to=upload_save_path_songs_path, help_text='请上传歌曲', verbose_name = '歌曲')
    lyric = models.FileField(upload_to=upload_save_path_songs_lyric, help_text='请上传歌曲单词', verbose_name = '歌词')
 
    # 设置与歌手表关联外键
    # 一对多外键设置在多的模型中
    singler = models.ForeignKey("Singler", on_delete=models.CASCADE, verbose_name = '歌手')

    def save(self, force_insert=False, force_update=False, using=None,
         update_fields=None):
        """ 重写save方法 处理歌曲时长 """

        if not self.duration:
            self.duration = 0

        super().save()
        path_name = str(self.path.name)
        if path_name.endswith(".mp3"):
            save_path = os.path.join(settings.MEDIA_ROOT, path_name)
            self.duration = get_duration_mp3(save_path)
        # 获取相应歌手单曲数
        singe_num = get_singe_singler_num(self.singler_id)
        # 更新相应歌手的单曲数
        Singler.objects.filter(pk=self.singler_id).update(singe_num=singe_num)
        super().save()

 
 
class Album(BaseModel):
    """ 专辑表 """
 
    def upload_save_path_album_cover(instance, filename):
        """ 上传文件保存路径 """

        return 'uploads/album_cover/' + str(int(time.time())) + '/{0}'.format(filename)

    class Meta:
        verbose_name = '专辑'
        verbose_name_plural = '专辑'
 
    name = models.CharField('专辑名称', max_length=50, help_text='请输入专辑名称')
    cover = models.ImageField('专辑封面', upload_to=upload_save_path_album_cover, help_text='请上传专辑封面图')
    desc = models.CharField('专辑描述', max_length=255, help_text='请输入专辑描述')
    single_num = models.IntegerField(default=0, editable=False)
 
    langs = [('国语', '国语'), ('普通话', '普通话'), ('英语', '英语'), ('日韩', '日韩')]
    single_lang = models.CharField('专辑语种', max_length=50, choices=langs, help_text='请选择专辑语种')
 
    # 设置与歌手表关联外键 一对多
    singler = models.ForeignKey("Singler", on_delete=models.CASCADE, verbose_name='歌手', help_text='请选择歌手')
 
    # 设置与单曲表关联外键 多对多
    Singe = models.ManyToManyField('Singe', verbose_name='单曲', help_text='请选择单曲')
 
    def save(self, force_insert=False, force_update=False, using=None,
         update_fields=None):
        """ 重写save方法 处理单曲数和歌手专辑数 """
    
        super().save()
    
        # 获取选中的单曲字典
        sing_set = self.Singe.all()
        single_num = len(sing_set)
        # 更新单曲数
        self.single_num = single_num
    
        # 获取所属歌手专辑数
        album_num = get_album_singler_num(self.singler_id)
    
        super().save()
        # 更新歌手表-专辑数
        Singler.objects.filter(pk=self.singler_id).update(album_num=album_num)


class Carousel(models.Model):
    """ 首页轮播图 """
    
    class Meta:
        verbose_name = '首页轮播图'
        verbose_name_plural = '首页轮播图'

    def upload_save_path_carousel_cover(instance, filename):
        """ 上传文件保存路径 """

        return 'uploads/carousel_cover/' + str(int(time.time())) + '/{0}'.format(filename)

    path = models.ImageField(upload_to=upload_save_path_carousel_cover, help_text='请选择上传首页轮播图', verbose_name = '首页轮播图')
    href = models.CharField(max_length=100, help_text='请输入点击图片后跳转路径', verbose_name = '跳转路径')


class SongCategory(models.Model):
    """ 歌曲类型表 """
    
    class Meta:
        verbose_name = '歌曲类型'
        verbose_name_plural = '歌曲类型'
    
    name = models.CharField(max_length=100, help_text='请输入类型名称', verbose_name = '类型名称')
    pid = models.IntegerField(default=0, help_text='父类型id', verbose_name = '父类型id')
 
 
class SongSheet(BaseModel):
    """ 歌单表 """
    
    def upload_save_path_sheet_cover(instance, filename):
        """ 上传文件保存路径 """

        return 'uploads/sheet_cover/' + str(int(time.time())) + '/{0}'.format(filename)

    class Meta:
        verbose_name = '歌单'
        verbose_name_plural = '歌单'
        
    name = models.CharField(max_length=100, help_text='请输入歌单名称', verbose_name = '歌单名称')
    cover = models.ImageField(upload_to=upload_save_path_sheet_cover, help_text='请上传歌单封面图', verbose_name = '歌单封面')
    playnum = models.IntegerField(default=0, help_text='请输入播放量', verbose_name = '播放量')
 
    # 歌曲类型与歌单表 多对多关系
    category = models.ManyToManyField('SongCategory', verbose_name = '歌曲类型')
 
    # 歌单表与单曲表多对多关系
    singe = models.ManyToManyField('Singe', verbose_name = '单曲')