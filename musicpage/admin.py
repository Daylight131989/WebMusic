from django.contrib import admin
from .models import Singler


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
    list_filter = ['name', 'constellation']
    # 搜索
    search_fields = ['name', 'constellation']
    # 分页
    list_per_page = 5


admin.site.register(Singler, SinglerAdmin)