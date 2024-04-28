from django.urls import path
from musicpage.views import index, home # python调包过程，在哪个文件中调用哪个函数

urlpatterns = [
    path('', index, name="index"), # path是一个解析的过程，
    path('home/', home, name="home"),
]