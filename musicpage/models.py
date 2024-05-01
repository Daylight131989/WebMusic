from django.db import models
from datetime import date, datetime
 
 
# Create your models here.
class Singler(models.Model):
    """ 歌手表模型 """
 
    name = models.CharField(max_length=50, help_text='请输入歌手名称')
    first_letter = models.CharField(max_length=15, help_text='请输入歌手名称首字母')
    # 设置上传位置
    portrait = models.ImageField(upload_to='uploads/%Y%m%d%H/', help_text='请上传歌手照片')
    birthday = models.DateField(default=date.today, help_text='请选择歌手生日')
    height = models.IntegerField(help_text='请输入歌手身高（cm）', default=0, blank=True)
    weight = models.IntegerField(help_text='请输入歌手体重（kg）', default=0, blank=True)
    constellation = models.CharField(max_length=50, help_text='请输入歌手星座')
    singe_num = models.IntegerField(default=0)
    album_num = models.IntegerField(default=0)
    desc = models.TextField(help_text='请输入歌手简介')
    addtime = models.DateTimeField(auto_now_add=True)
    updatetime = models.DateTimeField(auto_now=True)