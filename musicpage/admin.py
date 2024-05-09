from django.contrib import admin
from .models import Singler, Singe, Album, Carousel, SongCategory, SongSheet
from django.utils.html import format_html


# Register your models here.
class SinglerAdmin(admin.ModelAdmin):
    
    # 列表页属性
    def get_name(self):
        return self.name
    get_name.short_description = '歌手名称'
 
    def get_portrait(self):
        return format_html(
            '<img src="/media/{}" width="100px" height="100px"/>',
            self.portrait,
        )
    get_portrait.short_description = '歌手头像'
 
    def get_constellation(self):
        return self.constellation
    get_constellation.short_description = '星座'
 
    def get_height(self):
        if self.height < 1:
            return '——'
        else:
            return str(self.height) + 'cm'
    get_height.short_description = '身高'
    
    def get_weight(self):
        if self.weight < 1:
            return '——'
        else:
            return str(self.weight) + 'kg'
    get_weight.short_description = '体重'
 
    def get_addtime(self):
        return self.addtime
    get_addtime.short_description = '创建时间'
 
    def get_updatetime(self):
        return self.updatetime
    get_updatetime.short_description = '更新时间'
 
    # 显示字段
    list_display = ['id', get_name, get_portrait, get_constellation, get_height, get_weight, get_addtime, get_updatetime]
    # 过滤器
    list_filter = ['name']
    # 搜索
    search_fields = ['name']
    # 分页
    list_per_page = 10


class SingeAdmin(admin.ModelAdmin):
    # 列表页属性
    def get_name(self):
        return self.name
    get_name.short_description = '歌曲名称'

    def get_singler(self):
        return self.singler
    get_singler.short_description = '歌手'
    
    def get_duration(self):
        seconds = self.duration
        minutes, seconds = divmod(seconds, 60)
        duration_str = '{:02d}:{:02d}'.format(minutes, seconds)
        return duration_str
    get_duration.short_description = '歌曲时长'

    def get_addtime(self):
        return self.addtime
    get_addtime.short_description = '创建时间'

    def get_updatetime(self):
        return self.updatetime
    get_updatetime.short_description = '更新时间'

    # 显示字段
    list_display = ['id', get_name, get_singler, get_duration, get_addtime, get_updatetime]
    # 过滤器
    list_filter = ['name']
    # 搜索
    search_fields = ['name']
    # 分页
    list_per_page = 5


class AlbumAdmin(admin.ModelAdmin):
    # 列表页属性
    def get_name(self):
        return self.name
    get_name.short_description = '专辑名称'

    def get_cover(self):
        return format_html(
            '<img src="/media/{}" width="100px" height="100px"/>',
            self.cover,
        )
    get_cover.short_description = '专辑封面'

    def get_singler(self):
        return self.singler
    get_singler.short_description = '歌手'

    def get_single_num(self):
        return self.single_num
    get_single_num.short_description = '单曲数'

    def get_single_lang(self):
        return self.single_lang
    get_single_lang.short_description = '语种'

    def get_addtime(self):
        return self.addtime
    get_addtime.short_description = '创建时间'

    def get_updatetime(self):
        return self.updatetime
    get_updatetime.short_description = '更新时间'

    # 显示字段
    list_display = ['id', get_name, get_cover, get_singler, get_single_num, get_single_lang, get_addtime, get_updatetime]
    # 过滤器
    list_filter = ['name', 'single_lang']
    # 搜索
    search_fields = ['name', 'single_lang']
    # 分页
    list_per_page = 5


class CarouselAdmin(admin.ModelAdmin):
    # 列表页属性
    def get_path(self):
        return format_html(
            '<img src="/media/{}" width="200px" height="100px"/>',
            self.path
        )
    get_path.short_description = '图片路径'
 
    def get_href(self):
        return self.href
    get_href.short_description = '跳转路径'
 
    # 显示字段
    list_display = ['id', get_path, get_href]


class SongCategoryAdmin(admin.ModelAdmin):
 
    def get_name(self):
        return self.name
    get_name.short_description = '类型名称'
 
    def get_pid(self):
        categoryChoice = [
            (0, '默认'),
            (1, '主题'),
            (2, '心情'),
            (3, '场景'),
            (4, '年代'),
            (5, '曲风流派'),
            (6, '语言')
        ]
        for index, item in categoryChoice:
            if index == self.pid:
                return item
    get_pid.short_description = '类型父id'
 
    # 显示字段
    list_display = ['id', get_name, get_pid]
    # 过滤器
    list_filter = ['name', 'pid']
    # 搜索
    search_fields = ['name']
    # 分页
    list_per_page = 10
 
 
class SongSheetAdmin(admin.ModelAdmin):
 
    def get_name(self):
        return self.name
 
    get_name.short_description = '类型名称'
 
    def get_cover(self):
        return format_html(
            '<img src="/media/{}" width="100px" height="100px"/>',
            self.cover,
        )

    get_cover.short_description = '歌单封面'

    def get_desc(self):
        return self.desc
 
    get_desc.short_description = '歌单描述'

    def get_playnum(self):
        return self.playnum
 
    get_playnum.short_description = '播放量'
 
 
    def get_addtime(self):
        return self.addtime
 
    get_addtime.short_description = '创建时间'
 
    def get_updatetime(self):
        return self.updatetime

    get_updatetime.short_description = '编辑时间'
 
    # 显示字段
    list_display = ['id', get_name, get_cover, get_desc, get_playnum, get_addtime, get_updatetime]
    # 过滤器
    list_filter = ['name']
    # 搜索
    search_fields = ['name']
    # 分页
    list_per_page = 10
 

admin.site.register(Singler, SinglerAdmin)
admin.site.register(Singe, SingeAdmin)
admin.site.register(Album, AlbumAdmin) 
admin.site.register(Carousel, CarouselAdmin)
admin.site.register(SongCategory, SongCategoryAdmin)
admin.site.register(SongSheet, SongSheetAdmin)