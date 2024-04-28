from django.http import HttpResponse

def index(request): # 每一个从前端过来的页面都会有一个request，会存我们很多的页面信息
    line1 = '<h1 style="text-align: center">我的第一个网页</h1>'
    return HttpResponse(line1) #返回一个字符串

def home(request):
    line1 = '<h1 style="text-align: center">用户主界面</h1>'
    return HttpResponse(line1)