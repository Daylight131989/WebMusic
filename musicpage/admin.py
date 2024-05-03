from django.contrib import admin
from .models import Singler, Singe, Album, Carousel, SongCategory, SongSheet


# Register your models here.
class SinglerAdmin(admin.ModelAdmin):
    
    # 列表页属性
    def get_name(self):
        return self.name
    get_name.short_description = '歌手名称'
 
    def get_portrait(self):
        return self.portrait
    get_portrait.short_description = '歌手头像'
 
    def get_constellation(self):
        return self.constellation
    get_constellation.short_description = '星座'
 
    def get_height(self):
        return str(self.height) + 'cm'
    get_height.short_description = '身高'
 
    def get_weight(self):
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
    list_per_page = 5


class SingeAdmin(admin.ModelAdmin):
    # 列表页属性
    def get_name(self):
        return self.name
    get_name.short_description = '歌曲名称'
    
    def get_duration(self):
        return self.duration
    get_duration.short_description = '歌曲时长'

    def get_addtime(self):
        return self.addtime
    get_addtime.short_description = '创建时间'

    def get_updatetime(self):
        return self.updatetime
    get_updatetime.short_description = '更新时间'

    # 显示字段
    list_display = ['id', get_name, get_duration, get_addtime, get_updatetime]
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

    def get_single_num(self):
        return self.singe_num
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
    list_display = ['id', get_name, get_single_num, get_single_lang, get_addtime, get_updatetime]
    # 过滤器
    list_filter = ['name', 'single_lang']
    # 搜索
    search_fields = ['name', 'single_lang']
    # 分页
    list_per_page = 5


class CarouselAdmin(admin.ModelAdmin):
    # 列表页属性
    def get_path(self):
        return self.path
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
        return self.pid
 
    get_pid.short_description = '类型父id'
 
    # 显示字段
    list_display = ['id', get_name, get_pid]
    # 过滤器
    list_filter = ['name']
    # 搜索
    search_fields = ['name']
    # 分页
    list_per_page = 10
 
 
class SongSheetAdmin(admin.ModelAdmin):
 
    def get_name(self):
        return self.name
 
    get_name.short_description = '类型名称'
 
    def get_cover(self):
        return self.cover
 
    get_cover.short_description = '歌单封面'
 
 
    def get_addtime(self):
        return self.addtime
 
    get_addtime.short_description = '创建时间'
 
    def get_updatetime(self):
        return self.updatetime
 
    # 显示字段
    list_display = ['id', get_name, get_cover]
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